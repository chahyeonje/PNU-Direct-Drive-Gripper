# PNU-Direct-Drive-Gripper
- Hyeonje Cha, guswp3611@gmail.com
- Jaehoon An, dkswogns46@gmail.com
- Inho Lee, inholee8@pusan.ac.kr
- Jungwon Seo, junseo.kr@pusan.ac.kr

## 1. Overview

## 2. Hardeware
- motor : t-motor gb54-2 (https://store.tmotor.com/goods-445-GB54-2.html)
- motor driver : odrive s1 (https://odriverobotics.com/shop/odrive-s1)
-----
## 3. Software
Our software is implemented with **python3** and tested on **Ubuntu**. You can also refer to this website https://docs.odriverobotics.com/v/latest/guides/getting-started.html.

### Versions ###
- ubuntu : 20.04
- Python : 3.10.11 (pyenv)
- Odrive control untility : 0.6.7

### Getting started ###
1. First, you should install accompanying PC program for the ODrive, 'odrivetool'.
```bash
pip install --upgrade odrive
```
2. Set up USB device permissions.
```bash
sudo bash -c "curl https://cdn.odriverobotics.com/files/odrive-udev-rules.rules > /etc/udev/rules.d/91-odrive.rules && udevadm control --reload-rules && udevadm trigger"
```
3. To launch the main interactive ODrive tool, type 'odrivetool'. And then, type 'odrv0.vbus_voltage' to inspect the boards main supply voltage.
```bash
odrivetool
```
&nbsp;&nbsp;&nbsp;&nbsp;If the program is installed and the odrive is connected successfully, then you can see the messages.
```bash
ODrive control utility v0.6.7
Please connect your ODrive
You can also type help() or quit().

Connected to ODrive S1 384D34783539 (firmware v0.6.7) as odrv0
In  [1]: odrv0.vbus_voltage
Out [1]: 23.931137084960938
```
-----
