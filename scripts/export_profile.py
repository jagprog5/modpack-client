#!/usr/bin/env python3

import argparse
import os
import zipfile
from io import BytesIO

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
OVERRIDES_PATH = os.path.join(SCRIPT_DIR, '..', 'overrides')
MANIFEST_PATH = os.path.join(SCRIPT_DIR, '..', 'manifest.json')

parser = argparse.ArgumentParser(description="Export the profile into a zip file.")
parser.add_argument('output_path', nargs='?', default='profile.zip',
                    help="Output zip file path (default: profile.zip)")
args = parser.parse_args()


# Collect all files to add to the final zip
files_to_add = []

# Add manifest.json
files_to_add.append(('manifest.json', MANIFEST_PATH))

# Process overrides
for root, dirs, files in os.walk(OVERRIDES_PATH):
    for d in dirs[:]:  # iterate over a copy since we may remove entries while iterating
        dir_path = os.path.join(root, d)
        rel_dir = os.path.relpath(dir_path, OVERRIDES_PATH)
        # zip folders ending with .rcst
        if rel_dir.startswith('structures') and d.endswith('.rcst'):
            buf = BytesIO()
            with zipfile.ZipFile(buf, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
                for r, _, fs in os.walk(dir_path):
                    for f in fs:
                        abs_path = os.path.join(r, f)
                        rel_path = os.path.relpath(abs_path, dir_path)
                        zf.write(abs_path, arcname=rel_path)
            buf.seek(0)
            rcst_bytes = buf.read()
            # save as overrides/structures/.../<folder>.rcst
            arcname = os.path.join('overrides', rel_dir)
            files_to_add.append((arcname, rcst_bytes))
            dirs.remove(d)  # skip walking this folder further

    for file in files:
        abs_file = os.path.join(root, file)
        rel_file = os.path.relpath(abs_file, OVERRIDES_PATH)
        # skip files inside folders we zipped
        if any(rel_file.startswith(f"structures/{d}") for d in dirs if d.endswith('.rcst')):
            continue
        arcname = os.path.join('overrides', rel_file)
        files_to_add.append((arcname, abs_file))

# Write the final profile zip
with zipfile.ZipFile(args.output_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
    for arcname, source in files_to_add:
        if isinstance(source, bytes):
            zf.writestr(arcname, source)
        else:
            zf.write(source, arcname)
