#!/usr/bin/env python3
# used by import_automation.sh
import argparse, os, json
default_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", 'manifest.json')
parser = argparse.ArgumentParser(description="Sorts the entries by projectID, for better organization and git diffs.")
parser.add_argument('-p', '--path', 
                    type=str, 
                    default=default_path, 
                    help='Specify the path to the manifest file. Default is <script_dir>/../manifest.json')
parser.add_argument('--manifest-version', 
                    type=int, 
                    help='Set the manifest version. Must be a non-negative integer.')
args = parser.parse_args()
with open(args.path, 'r+') as file:
    data = json.load(file)
    if not "files" in data:
        raise Exception(f'Error: "files" key not found in {args.path}')
    data["files"].sort(key=lambda x: x["projectID"])

    if args.manifest_version:
        if args.manifest_version < 0:
            raise ValueError("Manifest version must be a non-negative integer.")
        data["manifestVersion"] = args.manifest_version
    file.seek(0)
    json.dump(data, file, indent=2)
    file.truncate()
