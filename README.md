# Automatic door open system using face recognition
_by KIM Hyun-hee, JEON Seoung-hoon, YOON Young-sang_
* * *

#### Description
It's a system that automatically opens door through face recognition.  
When the door is opened, A person who entered is sent a text message via telegram.

#### Environment
Rasberry Pi 3  
OS : Ubuntu Mate 16.04 LTS  
Requirements : OpenCV 3.1.0, Python 3.5  

PC  
OS : Ubuntu Desktop 16.04 LTS  
Requirements : OpenCV 3.1.0, Openface API, Dlib, Torch, Telegram, Python 3.5
  
#### Contents
- [OS Installation](#INSTALL)

- [Configuration](#CONFIGURATION)
  - [Rasberry Pi](#RASP)
  - [Server PC](#SERVER)

- [Creating a Telegram Bot](#TELEGRAM)

- [Source Code](#CODE)

- [Execution](#EXECUTION)

<a id="INSTALL"></a> 
## OS Installation 
> coming soon!

<a id="CONFIGURATION"></a>
## Configuration

 <a id="RASP"></a>
 - ### Rasberry Pi 
 1. Basic
 ```
 coming soon!
 ```
 2. OpenCV
 ```
 coming soon!
 ```

<a id="SERVER"></a>
 - ### Server PC
 1. Basic
 ```
 $ sudo apt-get update
 $ sudo apt-get upgrade
 
 $ sudo apt-get -y install build-essential cmake git pkg-config
 $ sudo apt-get -y install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
 $ sudo apt-get -y install libgtk2.0-dev libgtk-3-dev
 $ sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
 $ sudo apt-get -y install libatlas-base-dev gfortran
 $ sudo apt-get -y install libeigen3-dev python3-dev python3-pip python3-numpy
 ```
 2. OpenCV
 ```
 $ wget -O opencv.zip https://github.com/opencv/opencv/archive/3.1.0.zip
 $ unzip opencv.zip
 
 $ wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.1.0.zip
 $ unzip opencv_contrib.zip
 
 $ cd opencv-3.1.0
 $ mkdir build
 $ cd build
 
 Its' not finished.
 ```
 
 3. Dlib
 ```
 coming soon!
 ```
 
 4. Torch
 ```
 coming soon!
 ```
 
 5. Openface
 ```
 coming soon!
 ```
 
 6. Telepot
 ```
 coming soon!
 ```
 
<a id="TELEGRAM"></a>
## Creating a Telegram Bot 
> coming soon!

<a id="CODE"></a>
## Source Code 
> coming soon!

<a id="EXECUTION"></a>
## Execution
> coming soon!
