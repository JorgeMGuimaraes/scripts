#!/usr/bin/env bash

xrandr --output "$(xrandr | awk '/ connected/{print $1; exit; }')" --auto