#!/bin/bash

# an automation helper which populates manifest.json and modlist.md from a curseforge profile (profile.zip)
# this does not handle anything else (configs, etc)

set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd -- "$SCRIPT_DIR/.."
mkdir profile_temp
unzip profile.zip -d profile_temp
trap 'rm -rf profile_temp' EXIT

manifest_version=$(cat manifest.json | jq .manifestVersion)
manifest_version=$((manifest_version + 1))

cp profile_temp/manifest.json ./manifest.json
./scripts/format_manifest.py --manifest-version "$manifest_version"

cp profile_temp/modlist.html ./modlist.md

first_line=$(head -n 1 modlist.md)
last_line=$(tail -n 1 modlist.md)
middle_lines=$(sed '1d;$d' modlist.md | sort)

printf "%s\n" "$first_line" > modlist.md
printf "%s\n" "$middle_lines" >> modlist.md
printf "%s\n" "$last_line" >> modlist.md

rm -rf profile_temp
rm profile.zip
