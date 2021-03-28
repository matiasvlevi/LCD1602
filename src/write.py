#! /usr/bin/env python
from module import LCD1602 as LCD
import sys

arg = sys.argv

try:
    LCD.init(0x27, 1)
except:
    print("Error loading LCD1602 screen. Try changing the screen adress.")
    print("You can see your LCD adress with 'i2cdetect -y 1'.")

def write(line1,line2):
    if len(line1) > 16 or len(line2) > 16:
        print("Can't display strings with a length of more than 16...")
        quit()
    else:
        LCD.write(0,0,line1)
        LCD.write(0,1,line2)
        print("Successfully displayed strings on LCD display")
        quit()

if len(arg) == 1:
    print("No string arguments were specified...")
    quit()
else:
    if len(arg) == 2:
        arg.extend([""])
        
    write(arg[1],arg[2])
