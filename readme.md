# Easy Scripts
Some Python scritps to make life a bit easier.

## Setup (deprecated)

1. Clone this git;
2. Edit `.profile` and copy the last lines from 'config/.profile' or replace if everything else is the same;
3. Reload profile: `. ~/.profle`;
4. Run script.

>* Backup old file before overwrite

## Bash General

### Check battery status
`check_battery_status.sh`

Notify user if battery level is less than a threshold.
>* Default: 30%
>* Ubuntu only

### Caff (Caffeine)
`caff.sh time`

Prevent computer from sleep an amount of time.

>* Usage: `caff.sh 25` for 25 minutes;
>* ref:
https://www.gregjs.com/linux/2016/linux-tip-of-the-day-temporarily-prevent-your-screen-from-going-to-sleep/

### Update System

`update_system.sh`

Run apt update, upgrade, autoremove and clean sequentially.

>* Usage: just run `update_system.sh`.

## Bash VM

### VM Resize

`vmresize.sh`

Resize linux guest screen to fit host qemu window.

>* Usage `vmresize.sh`
>* Shortcut to `xrandr --output Monitor --auto`, where 'Monitor' is a virtual display get programatically.

## Docker
Docker bash scripts, composer recipes or related files.

### Lamp Server
`start_docker_lamp.sh path`

Start a Docker Lamp Server in local path if no path is provided.

>* Provide a path, or local path will be used;
>* Create an `app` subfolder to hold project files and folders (html, php, img/, etc);
>* Docker-LAMP comes pre-installed with phpMyAdmin available from http://DOCKER_ADDRESS/phpmyadmin;
>* ref: https://hub.docker.com/r/mattrayner/lamp

## Config
Various system/ software configuration files.

### User Profile
`.profile`

Executed before bash loads.

>* Path: `~/.profile`
>* Backup old file before overwrite

## History

* 2020-11-02: Start moving from Bash to Python, from multiple subfolders to one single folder