#! /usr/bin/env python3
"""Utilities"""
import json
import subprocess
import sys
from os import system
from typing import Dict, List

class bcolors:
    HEADER      = '\033[95m'
    OKBLUE      = '\033[94m'
    OKCYAN      = '\033[96m'
    OKGREEN     = '\033[92m'
    WARNING     = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'

def run(cmds:List[str]):
    '''Run a list of shell commands and arguments'''
    for cmd in cmds:
        print(f'{bcolors.OKGREEN}$ {cmd}{bcolors.ENDC}')
    for cmd in cmds:
        system(cmd)
    return

def get_process(args:list):
    '''Run a subprocess and return a 'CompletedProcess'.'''
    return subprocess.run(
        args                =args,
        universal_newlines  =True,
        stdout              =subprocess.PIPE,
        stderr              =subprocess.PIPE,
        check               =True,
        )

def is_help_needed() -> bool:
    '''Check if user entered a help token.'''
    return sys.argv[1] == '--help' or sys.argv[1] == '-h'

def show_help(script_name: str):
    '''Print help file'''
    try:
        file_name = f'{script_name}-man'
        with open(file=file_name, mode='r', encoding='utf8') as f:
            for line in f:
                print(line.strip('\n'))
    except FileNotFoundError:
        print('Help file does not exist.')
    return

def load_data(file_name: str) -> List[Dict[str, str]]:
    """Load data from a json file."""
    try:
        with open(file_name, encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f"{bcolors.FAIL}File not found: {file_name}.{bcolors.ENDC}")
        exit()
