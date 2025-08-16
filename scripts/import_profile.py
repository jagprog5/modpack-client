#!/usr/bin/env python3

import subprocess
import argparse
import os
import json
import zipfile
import shutil
import re
from io import BytesIO

# Constants
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
MANIFEST_OUTPUT_PATH = os.path.join(SCRIPT_DIR, '..', 'manifest.json')
MODLIST_OUTPUT_PATH = os.path.join(SCRIPT_DIR, '..', 'modlist.md')
OVERRIDES_OUTPUT_PATH = os.path.join(SCRIPT_DIR, '..', 'overrides')

parser = argparse.ArgumentParser(
    description=(
        "Copies a CurseForge profile into this repo in a git-friendly way.\n\n"
        "Imports manifest.json and modlist.html\n"
        "Imports the following files and folders from the profile's overrides:\n"
        "  - config/ *\n"
        "  - resources/\n"
        "  - scripts/\n"
        "  - shaderpacks/\n"
        "  - structures/\n"
        "* Each config file in overrides/config/ is only imported if it already exist "
        "in this repo or matchs --new-override-cfg."
    ), formatter_class=argparse .RawTextHelpFormatter
)
parser.add_argument('profile_path', help='The path to the input file.')
parser.add_argument('--new-override-cfg', type=str, default='',
    help=(
        "Config files are not imported from the profile if they aren't already in this repo\n"
        "(because many configs just use their default and don't need to be stated).\n"
        "If a config file is changed which does not already exist here, match it in this arg,\n"
        "in the form of a regex. For example: mobends/.*\n"
    )
)
parser.add_argument('--include', type=str, default='',
    help=(
        "The above folders and files are imported.\n"
        "This regex restricts that list further (only import a subset).\n"
        "For example: scripts/.*"
    )
)

parser.add_argument('--exclude', type=str, default='',
    help='Similar to --include')

args = parser.parse_args()

# Compile regexes
include_regex = re.compile(args.include) if args.include else None
exclude_regex = re.compile(args.exclude) if args.exclude else None

# Get the old manifest version and increment
result = subprocess.run(
    ["git", "show", "HEAD:manifest.json"],
    capture_output=True,
    text=True,
    check=True
)
output_manifest_version = int(json.loads(result.stdout)["manifestVersion"]) + 1

non_config_overrides_found = set()

with zipfile.ZipFile(args.profile_path, 'r') as zip_ref:
    for member in zip_ref.namelist():
        if member == "manifest.json":
            with zip_ref.open(member) as f:
                manifest_data = json.load(f)
            manifest_data["manifestVersion"] = output_manifest_version
            manifest_data["files"].sort(key=lambda x: x["projectID"])
            with open(MANIFEST_OUTPUT_PATH, 'w') as f:
                json.dump(manifest_data, f, indent=2)
        elif member == "modlist.html":
            with zip_ref.open(member) as f:
                lines = f.read().decode("utf-8").splitlines()
            if len(lines) >= 2:
                first_line = lines[0]
                last_line = lines[-1]
                middle_lines = sorted(lines[1:-1])
                new_lines = [first_line] + middle_lines + [last_line]
            else:
                new_lines = lines
            with open(MODLIST_OUTPUT_PATH, 'w', encoding="utf-8") as out_f:
                out_f.write("\n".join(new_lines) + "\n")
        elif member.startswith("overrides/"):
            relative_path = os.path.relpath(member, "overrides")
            target_path = os.path.join(OVERRIDES_OUTPUT_PATH, relative_path)

            # apply the global include and exclude
            if include_regex and not include_regex.fullmatch(relative_path):
                continue

            if exclude_regex and exclude_regex.fullmatch(relative_path):
                continue

            should_be_copied = False
            if member.startswith("overrides/config/"):
                # most configs are left as their default. this is done by not
                # stating the file at all! special mechanism (arg) for if new
                # cfg is to be added to the pack
                should_be_copied = os.path.exists(target_path) or re.fullmatch(args.new_override_cfg, member[len("overrides/config/"):])
            else:
                allowed_overrides = [ 'resources', 'scripts', 'shaderpacks', 'structures', ]
                for allowed_override in allowed_overrides:
                    if member.startswith("overrides/" + allowed_override + '/'):
                        should_be_copied = True
                        break
                if should_be_copied:
                    non_config_override_element = member.split(os.sep)[1]
                    if non_config_override_element not in non_config_overrides_found:
                        non_config_overrides_found.add(non_config_override_element)
                        full_path = os.path.join(OVERRIDES_OUTPUT_PATH, non_config_override_element)
                        if os.path.exists(full_path):
                            if os.path.isdir(full_path):
                                shutil.rmtree(full_path)
                            else:
                                os.remove(full_path)

            if should_be_copied:
                if member.startswith("overrides/structures/") and member.endswith(".rcst"):
                    # special handling of recurrent complex structure files
                    os.makedirs(target_path, exist_ok=True)
                    with zip_ref.open(member) as rcst_file:
                        rcst_data = rcst_file.read()
                    with zipfile.ZipFile(BytesIO(rcst_data)) as inner_zip:
                        for inner_member in inner_zip.namelist():
                            inner_target_path = os.path.join(target_path, inner_member)
                            os.makedirs(os.path.dirname(inner_target_path), exist_ok=True)
                            with inner_zip.open(inner_member) as inner_source, \
                                open(inner_target_path, 'wb') as inner_target:
                                inner_target.write(inner_source.read())
                else:
                    os.makedirs(os.path.dirname(target_path), exist_ok=True)
                    with zip_ref.open(member) as source:
                        raw_data = source.read()
                    try:
                        text_data = raw_data.decode('utf-8')
                        text_data = text_data.replace('\r\n', '\n').replace('\r', '\n')
                        with open(target_path, 'w', encoding='utf-8', newline='\n') as target:
                            target.write(text_data)
                    except UnicodeDecodeError:
                        with open(target_path, 'wb') as target:
                            target.write(raw_data)
