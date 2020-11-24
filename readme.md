# Lazy Scr

Because  we're too lazy to write *Scripts*. 
Some Python scripts to make life a bit easier by bundling linux commands together with less typing and easy to remember names.

## Setup (deprecated)
> Make sure you have Python 3.6+ installed.
1. Clone this git;
2. Edit `.profile` and copy the last lines from 'config/.profile' or replace if everything else is the same;
3. Reload profile: `. ~/.profle`;
4. Run scripts.

>* Backup old files before overwrite

## General
These scripts were designed to work on Linux systems. May work on MacOS? I don't know.

As said before, all writen in Python, most because it's easier to write funcions than in Bash or similar, easier to debug, easier to find help...

## Scripts

Here is alist of what you can find here:

### Update System

`update_system`

Performs:
* update repository lists,
* upgrade installed software,
* autoremove and clean cache data.

Uses different tools for different OSes, for now, `apt` for Debian/Ubuntu and `pacman` for Arch Linux.

>* Usage: just run `update_system`.

### Resize Screen

`resize-screen`

Resize linux guest screen to fit host qemu window.

>* Usage `resize-screen`
>* Shortcut to `xrandr --output Monitor --auto`, where 'Monitor' is a virtual display get programatically.

## To do

* Installation script
* update-system-
* Explain how man works

## History

2020-11-10:
- update-time added;
- Todo list added to readme;

2020-11-02:
- Start moving from Bash to Python, from multiple subfolders to one single folder.