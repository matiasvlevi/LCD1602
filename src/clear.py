!# /usr/bin/env python
from module import LCD1602 as LCD

try:
    LCD.init(0x27, 1)
    LCD.clear()
    print("Successfully cleared the lcd screen!")
except:
    print("Error clearing the lcd screen...")

quit()
