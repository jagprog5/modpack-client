#!/usr/bin/env python3
# used by the CI
import argparse, os, json
default_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", 'manifest.json')
parser = argparse.ArgumentParser(description="Gets the manifest version.")
parser.add_argument('-p', '--path', 
                    type=str, 
                    default=default_path, 
                    help='Specify the path to the manifest file. Default is <script_dir>/../manifest.json')
args = parser.parse_args()
with open(args.path, 'r') as file:
    data = json.load(file)
    print(data['manifestVersion'])
