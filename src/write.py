!# /usr/bin/env python

import sys
import ..LCD1602 as LCD

arg = sys.argv

LCD.init(0x27, 1)

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
