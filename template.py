#! /usr/bin/env python

import sys
from utils import run, get_process, is_help_needed, show_help


commands = ['ls', '-la']

def do():
    commands = ['ls', '-la']
    run(commands)
    return

def start():
    if len(sys.argv) == 1:
        return
    if is_help_needed():
        show_help('')
        return
    return

start()
do()