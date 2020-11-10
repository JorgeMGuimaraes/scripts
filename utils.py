#! /usr/bin/env python3
import subprocess
import sys


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