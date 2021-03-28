!# /usr/bin/env python
import ..LCD1602 as LCD
import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def display():
    LCD.init(0x27, 1)
    LCD.write(0,0,"WLAN0:")
    LCD.write(0,1,get_ip())

display()
quit()
