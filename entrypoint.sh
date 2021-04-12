#!/bin/bash
service mysql restart
mysql -uroot -pCizoo123* --port 3308 -e"CREATE DATABASE cizoodb" -vvv
mysql -uroot -pCizoo123* --port 3308 -e"ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Cizoo123*'"
service nginx restart
python3 settings.py
python3 video.py
