#! /usr/bin/env python
import subprocess
import sys


def run(args:list):
    '''Run a list of shell commands and arguments'''
    _ = subprocess.run(args=args)
    return

def get_process(args:list):
    '''Run a subprocess and return a 'CompletedProcess'.'''
    return subprocess.run(
        args                =args,
        check               =True,
        stdout              =subprocess.PIPE,
        universal_newlines  =True
        )

def is_help_needed() -> bool:
    '''Check if user entered a help token.'''
    return sys.argv[1] == '--help' or sys.argv[1] == '-h'

def show_help():
    '''Print all help messages'''
    print('help message')
    return