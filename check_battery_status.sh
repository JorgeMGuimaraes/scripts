battery_level=`acpi -b | grep -P -o '[0-9]+(?=%)'`
threshold=25
if [ $battery_level -le $threshold ]
then
    notify-send "Battery low" "Battery level is ${battery_level}%!"
fi
