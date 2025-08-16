#!/usr/bin/env python3

'''
This converts a Minecraft Java Edition .nbt tile into a human readable json.
It's a single python file that only uses the stdlib.

It does some sparse encoding and decompression - whatever I though was best!

This was mostly AI generated, following this
[repo](https://github.com/midnightfreddie/nbt2json). But reducing the scope and
making a bunch of changes.

It's intended for [git
textconv](https://git-scm.com/docs/gitattributes#_customizing_word_diff), which
is a feature that allows human readable diffs on binary files:

.gitattributes *.nbt diff=nbt

git config diff.nbt.textconv "python3 scripts/nbt_textconv.py"
'''
#!/usr/bin/env python3
import argparse
import gzip
import io
import json
import math
import struct
import sys

BYTE_ORDER = ">"  # Java Edition NBT is big-endian

class NbtParseError(Exception):
    pass

def read_struct(fmt, f):
    size = struct.calcsize(fmt)
    data = f.read(size)
    if len(data) != size:
        raise NbtParseError(f"Unexpected end of data reading format {fmt}")
    return struct.unpack(fmt, data)[0]

def read_string(f):
    length = read_struct(BYTE_ORDER + "h", f)
    data = f.read(length)
    if len(data) != length:
        raise NbtParseError(f"Unexpected end of data reading string of length {length}")
    return data.decode("utf-8", errors="replace")

def value_to_json_number(n):
    return str(n)

def value_to_json_string(s):
    return json.dumps(s)

def payload_to_jsonish(f, tag_type):
    if tag_type == 0:
        return ""
    elif tag_type == 1:  # byte
        return value_to_json_number(read_struct(BYTE_ORDER + "b", f))
    elif tag_type == 2:  # short
        return value_to_json_number(read_struct(BYTE_ORDER + "h", f))
    elif tag_type == 3:  # int
        return value_to_json_number(read_struct(BYTE_ORDER + "i", f))
    elif tag_type == 4:  # long
        return value_to_json_number(read_struct(BYTE_ORDER + "q", f))
    elif tag_type == 5:  # float
        return value_to_json_number(read_struct(BYTE_ORDER + "f", f))
    elif tag_type == 6:  # double
        d = read_struct(BYTE_ORDER + "d", f)
        if math.isnan(d):
            return value_to_json_string("NaN")
        return value_to_json_number(d)
    elif tag_type == 7:  # byte array
        length = read_struct(BYTE_ORDER + "i", f)
        raw = f.read(length)
        if len(raw) != length:
            raise NbtParseError("Unexpected end reading TAG_Byte_Array contents")
        vals = struct.unpack(BYTE_ORDER + f"{length}b", raw)
        return "[" + ",".join(value_to_json_number(v) for v in vals) + "]"
    elif tag_type == 8:  # string
        return value_to_json_string(read_string(f))
    elif tag_type == 9:  # list
        elem_type = read_struct(BYTE_ORDER + "b", f)
        length = read_struct(BYTE_ORDER + "i", f)
        items = [payload_to_jsonish(f, elem_type) for _ in range(length)]
        return "[" + ",".join(items) + "]"
    elif tag_type == 10:  # compound
        parts = []
        while True:
            next_type = read_struct(BYTE_ORDER + "b", f)
            if next_type == 0:
                break
            name = read_string(f)
            val = payload_to_jsonish(f, next_type)
            parts.append(f"{value_to_json_string(name)}:{val}")
        return "{" + ",".join(parts) + "}"
    elif tag_type == 11:  # int array
        length = read_struct(BYTE_ORDER + "i", f)
        raw = f.read(length * 4)
        if len(raw) != length * 4:
            raise NbtParseError("Unexpected end reading TAG_Int_Array contents")
        vals = struct.unpack(BYTE_ORDER + f"{length}i", raw)
        return "[" + ",".join(value_to_json_number(v) for v in vals) + "]"
    elif tag_type == 12:  # long array
        length = read_struct(BYTE_ORDER + "i", f)
        raw = f.read(length * 8)
        if len(raw) != length * 8:
            raise NbtParseError("Unexpected end reading TAG_Long_Array contents")
        vals = struct.unpack(BYTE_ORDER + f"{length}q", raw)
        return "[" + ",".join(value_to_json_number(v) for v in vals) + "]"
    else:
        raise NbtParseError(f"TagType {tag_type} not recognized")

def read_one_root_payload(buf):
    if buf.tell() >= len(buf.getbuffer()):
        return None
    tag_type = read_struct(BYTE_ORDER + "b", buf)
    if tag_type == 0:
        return None
    _root_name = read_string(buf)
    return payload_to_jsonish(buf, tag_type)

def nbt_to_jsonish(data_bytes):
    buf = io.BytesIO(data_bytes)
    payloads = []
    while True:
        payload = read_one_root_payload(buf)
        if payload is None:
            break
        payloads.append(payload)
    if not payloads:
        return "null"
    if len(payloads) == 1:
        return payloads[0]
    return "[" + ",".join(payloads) + "]"

def sparsify_metadata(obj):
    if isinstance(obj, dict):
        return {k: sparsify_metadata(v) if k != "metadata" else _sparse_list(v)
                for k, v in obj.items()}
    elif isinstance(obj, list):
        return [sparsify_metadata(v) for v in obj]
    else:
        return obj

def _sparse_list(lst):
    if isinstance(lst, list):
        return {i: v for i, v in enumerate(lst) if v != 0}
    return lst

def decompress_blocks(blocks_compressed):
    data_bytes = blocks_compressed["data_bytes"]
    bit_length = blocks_compressed["data_bitLength"]
    total_values = blocks_compressed["data_length"]

    result = []
    buffer = 0
    bits_in_buffer = 0

    for byte in data_bytes:
        buffer = (buffer << 8) | byte
        bits_in_buffer += 8

        while bits_in_buffer >= bit_length and len(result) < total_values:
            bits_in_buffer -= bit_length
            value = (buffer >> bits_in_buffer) & ((1 << bit_length) - 1)
            result.append(value)

    return result

def dump_json(obj, indent=2):
    """Pretty-print JSON with inline metadata/blocks and nicely indented mapping."""
    def _dump(v, level=0, key=None):
        space = " " * (level * indent)
        if isinstance(v, dict):
            items = []
            for k, val in v.items():
                if k == "metadata":
                    items.append(f'{space}  "metadata":{json.dumps(val, separators=(",", ":"))}')
                elif k == "blocks":
                    items.append(f'{space}  "blocks":{json.dumps(val, separators=(",", ":"))}')
                elif k == "mapping" and isinstance(val, list):
                    items.append(f'{space}  "mapping": [\n' +
                                 ",\n".join(f'{space}    {json.dumps(item)}' for item in val) +
                                 f'\n{space}  ]')
                else:
                    items.append(f'{space}  {json.dumps(k)}: {_dump(val, level+1)}')
            return "{\n" + ",\n".join(items) + f"\n{space}}}"
        elif isinstance(v, list):
            if not v:
                return "[]"
            # Normal array: each element indented
            return "[\n" + ",\n".join(f"{space}  {_dump(i, level+1)}" for i in v) + f"\n{space}]"
        else:
            return json.dumps(v)
    print(_dump(obj))


def main():
    parser = argparse.ArgumentParser(description="Convert Minecraft NBT to JSON-like with sparse metadata.")
    parser.add_argument("nbt_file", help="Path to .nbt or .nbt.gz file")
    args = parser.parse_args()

    with open(args.nbt_file, "rb") as f:
        magic = f.read(2)
        f.seek(0)
        if magic == b"\x1f\x8b":
            with gzip.open(f, "rb") as gz:
                data = gz.read()
        else:
            data = f.read()

    out_str = nbt_to_jsonish(data)
    parsed_json = json.loads(out_str)
    parsed_json = sparsify_metadata(parsed_json)

    # Decompress blocksCompressed if present
    bc = parsed_json.get("blockCollection", {})
    if "blocks" in bc and isinstance(bc["blocks"], dict) and "blocksCompressed" in bc["blocks"]:
        bc["blocks"] = decompress_blocks(bc["blocks"]["blocksCompressed"])

    # Dump JSON with custom formatting
    dump_json(parsed_json, indent=2)

if __name__ == "__main__":
    main()
