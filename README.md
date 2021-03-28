# LCD1602 Python Bindings for Raspberry PI


<br/><br/>

#### Setup
Enable Raspberry PI's GPIO pins:
```sh
sudo usermod -a -G gpio your_username
```
Enable I2C in raspi-config:

```sh
sudo raspi-config #Interface Options > I2C > Enable(Yes)
```

Setup shell aliases: <br/>
```sh
# LCD1602/
sh alias.sh

# Aliases set to path /home/pi/LCD1602/src/
# Modify to set your own path if different.
```



<br/>

#### Install dependencies

```sh
# LCD1602/
sudo pip3 install -r requirements.txt
```

<br/><br/>

#### Usage

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

#### Usage (No alias)

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
