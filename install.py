#! /usr/bin/python3
"""Install utility cammands, shortcuts and scripts"""
import json
import shutil
from typing import List, Dict
from os.path import expandvars as p_expand, join as p_join

def install(path):
    """Install all files."""
    print('Installing...')
    for file in files_list(path)['rules']:
        shutil.copy(file['src'], p_join(p_expand(file['dest']), file['src']))
        print(f" {file['src']} Installed!...")
    print('All files installed.')

def files_list(path) -> List[Dict[str, str]]:
    """Return a list of files to be installed from json file."""
    try:
        with open(path, encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print('List of files to install not found')
        exit()

if __name__ == '__main__':
    install('install_files.json')
