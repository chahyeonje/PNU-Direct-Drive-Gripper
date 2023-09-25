# PNU-High-speed-scooping

## 1. Overview
This repository contains the software implementation of **High-Speed Scooping** using a [direct-drive gripper](https://github.com/HKUST-RML/ddh_hardware). It can be applied to rapidly picking thin objects off from a hard surface, which would be quite challenging with a straightforward approach aiming at directly obtaining a pinch grasp. See below for a comparison of our high-speed scooping with the traditional approach.
<!-- This repository contains the implementation of **High-Speed Scooping**, which refers to the task of picking up thin objects rapidly by interacting with the environment through a direct-drive gripper. Our scooping technique ensures a pinch grasp configuration can be obtained to pick up the object securely, which addresses the limitation of [**Smack and Snatch**](https://www.youtube.com/watch?v=xnHtb0XP3U4&ab_channel=ManipulationLab) that is unstable for grasping relatively thin objects, for example, plastic cards. -->


## 2. Prerequisites
### 2.1 Hardware

### 2.2 software
Our software is implemented with **python3** and tested on **Ubuntu**.
#### Versions ####
-----
- ubuntu : 20.04
- Python : 3.10.11 (pyenv)
- Odrive control untility : 0.6.7
#### Getting started ####
1. First, you should install accompanying PC program for the ODrive.
```bash
pip install --upgrade odrive
```


