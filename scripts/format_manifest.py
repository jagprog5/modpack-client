#!/usr/bin/env python3
import argparse, os, json
default_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", 'manifest.json')
parser = argparse.ArgumentParser(description="Sorts the entries by projectID, for better organization and git diffs.")
parser.add_argument('-p', '--path', 
                    type=str, 
                    default=default_path, 
                    help='Specify the path to the manifest file. Default is <script_dir>/../manifest.json')
args = parser.parse_args()
with open(args.path, 'r+') as file:
    data = json.load(file)
    if not "files" in data:
        raise Exception(f'Error: "files" key not found in {args.path}')
    data["files"].sort(key=lambda x: x["projectID"])
    file.seek(0)
    json.dump(data, file, indent=2)
    file.truncate()
