#!/bin/sh

sudo echo "alias lcdwrite='sudo python3 /home/pi/LCD1602/src/write.py'" >> /home/pi/.bashrc
echo 'Successfully set alias lcdwrite'

sudo echo "alias lcdclear='sudo python3 /home/pi/LCD1602/src/clear.py'" >> /home/pi/.bashrc
echo 'Successfully set alias lcdclear'

sudo echo "alias lcdhost='sudo python3 /home/pi/LCD1602/src/hostadress.py'" >> /home/pi/.bashrc
echo 'Successfully set alias lcdhost'
