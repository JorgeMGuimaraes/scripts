#! /usr/bin/python3
"""Install utility cammands, shortcuts and scripts"""
import shutil
from os import mkdir
from os.path import expandvars as p_expand, join as p_join, exists
from utils import load_data as files_list

def install(path: str) -> None:
    """Install all scripts, utilities and config files found at 'install_files.json'."""
    print('Installing...')
    for file in files_list(path)['rules']:
        file_path = p_expand(file['dest'])
        if not exists(file_path):
            try:
                mkdir(file_path)
            except OSError:
                print('Error creating directory: ' + file_path)
                exit()
        try:
            shutil.copy(file['src'], p_join(file_path, file['src']))
        except OSError:
            print('Error copying file: ' + file['src'])
            exit()
        print(f" {file['src']} Installed!")
    print('All files installed.')
    return

if __name__ == '__main__':
    install('install_files.json')
