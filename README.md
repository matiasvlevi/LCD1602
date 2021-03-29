# LCD1602
Python3 & Shell Bindings for 16 characters x 2 row LCD screen with the Raspberry PI & Raspbian OS.

<br/><br/>


## Hardware Setup

Connect pins to the rPI:

```
LCD1602        Raspberry PI
  GND --- to ----> GND
  VCC --- to ----> 5V
  SDA --- to ----> GPIO2
  SCL --- to ----> GPIO3
```

<br/>

## Software Setup


<br/>

Enable Raspberry PI's GPIO pins:
```sh
sudo usermod -a -G gpio your_username
```


<br/>

Enable I2C in raspi-config:

```sh
sudo raspi-config
# Interface Options > I2C > Enable(Yes)
```


<br/>

Setup shell aliases & install requirements: <br/>
```sh
# LCD1602/
source setup.sh
```
Aliases set to path `/home/pi/LCD1602/src/`. <br/>
Modify `/bash/alias.sh` to set your own path.



<br/><br/>

## Usage

<br/>

Write text on lcd screen:

```sh
lcdwrite "Text line 1" "Text line 2"
```

<br/>

Clear the lcd screen:

```sh
lcdclear
```

<br/>

Display wlan0 host ip adress:
```sh
lcdhost
```

<br/><br/>

## Usage (No alias)

<br/>

Write text on lcd screen:

```sh
# LCD1602/src/
sudo python3 write.py "Text line 1" "Text line 2"
```

<br/>

Clear the lcd screen:

```sh
# LCD1602/src/
sudo python3 clear.py
```

<br/>

Display wlan0 host ip adress:
```sh
# LCD1602/src/
sudo python3 hostadress.py
```

<br/><br/>
