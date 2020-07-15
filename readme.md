# Scripts
A series of Bash scripts to provide extended OS functionalities.

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