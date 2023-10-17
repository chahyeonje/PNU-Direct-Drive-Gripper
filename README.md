# PNU-Direct-Drive-Gripper
- Hyeonje Cha, guswp3611@gmail.com
- Jaehoon An, dkswogns46@gmail.com
- Inho Lee, inholee8@pusan.ac.kr
- Jungwon Seo, junseo.kr@pusan.ac.kr

## 1. Overview

## 2. Hardeware
### Bill of materials(BOM) ###
#### Off-the-shelf parts
- [T-motor gb54-2](https://store.tmotor.com/goods-445-GB54-2.html) X 4
- [Odrive s1](https://odriverobotics.com/shop/odrive-s1) X 4
- [AS5048A Encoder + solid magnet](https://ko.aliexpress.com/item/1005004239532357.html?spm=a2g0o.ppclist.product.16.189a33gr33grC1&pdp_npi=2%40dis%21KRW%21%E2%82%A9%2020%2C299%21%E2%82%A9%2020%2C299%21%21%21%21%21%402103011616813606980156478ed18f%2112000028490990365%21btf&_t=pvid%3A1729ba70-2e9e-4e62-ae44-2781def9d2bc&afTraceInfo=1005004239532357__pc__pcBridgePPC__xxxxxx__1681360698&gatewayAdapt=glo2kor) X 4
- [Bearing - outer-diameter = 100mm, inner-diamter = 6mm](https://kr.misumi-ec.com/vona2/detail/221000058378/?KWSearch=%eb%b2%a0%ec%96%b4%eb%a7%81&searchFlow=results2products) X 12
- [Dowel pin - diameter = 6mm, length = 10mm](https://ko.aliexpress.com/item/1005003326358562.html?spm=a2g0o.productlist.main.9.5f9d4520HPGHnd&algo_pvid=eee7164e-1d0b-425a-bb77-c06aaa2ae10c&aem_p4p_detail=202304140514266025200904223640004224758&algo_exp_id=eee7164e-1d0b-425a-bb77-c06aaa2ae10c-4&pdp_npi=3%40dis%21KRW%2113356.0%217080.0%21%21%21%21%21%40211bd8be16814744666117620d07da%2112000025228771502%21sea%21KR%210&curPageLogUid=YaY5cKEIVcXy&ad_pvid=202304140514266025200904223640004224758_5&ad_pvid=202304140514266025200904223640004224758_5) X 6
- Shielded cable
- 3-phase cable

#### 3D Printing ####
- [Adapter plate](adapter_plate.STL) X 4
- [Bearing spacer](bearing_spacer.STL) X 12
- [Calibration arm](calibration_arm.STL) X 1
- [Calibration stand](calibration_stand.STL) X 1
- [Coupler](coupler.STL) X 1
- [Couping](coupling.STL) X 1
- [Distal link](distal_link.STL) X 2
- [Distal tip link](distal_tip_link.STL) X 2
- [Finger tip](finger_tip.STL) X 2
- [Gripper shell](gripper_shell.STL) X 1
- [Magnet holder](stl/magnet_holder.STL) X 4
- [Motor plate](stl/motor_plate.STL) X 4
- [Proximal link](stl/proximal_link.STL) X 4
- The gripper is designed to be compatible with Rainbow robotics RB5. For other robot systems, it should be better that you design your own adapter plate and coupling.
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
