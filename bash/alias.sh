#!/bin/sh


#temp
alias lcdwrite='sudo python3 /home/pi/LCD1602/src/write.py'
sudo echo "alias lcdwrite='sudo python3 /home/pi/LCD1602/src/write.py'" >> /home/pi/.bashrc

echo 'Successfully set alias lcdwrite'


#temp
alias lcdclear='sudo python3 /home/pi/LCD1602/src/clear.py'
sudo echo "alias lcdclear='sudo python3 /home/pi/LCD1602/src/clear.py'" >> /home/pi/.bashrc

echo 'Successfully set alias lcdclear'


#temp
alias lcdhost='sudo python3 /home/pi/LCD1602/src/hostadress.py'
sudo echo "alias lcdhost='sudo python3 /home/pi/LCD1602/src/hostadress.py'" >> /home/pi/.bashrc

echo 'Successfully set alias lcdhost'
