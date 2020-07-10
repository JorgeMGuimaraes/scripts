sudo apt remove –purge php*
sudo apt purge php*
sudo apt autoremove
sudo apt autoclean
sudo apt remove dbconfig-php
sudo apt dist-upgrade
sudo dpkg --get-selections | grep php | cut -f 1