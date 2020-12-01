#! /usr/bin/env python3
import subprocess
import sys

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

def run(args:list):
    '''Run a list of shell commands and arguments'''
    _ = subprocess.call(args=args, shell=True)
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