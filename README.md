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
 $ sudo apt-get -y install libjpeg8-dev libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
 $ sudo apt-get -y install libgtk2.0-dev libgtk-3-dev
 $ sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev
 $ sudo apt-get -y install libv4l-dev v4l-utils
 $ sudo apt-get -y install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
 $ sudo apt-get -y install libqt4-dev
 $ sudo apt-get -y install libatlas-base-dev gfortran libeigen3-dev
 $ sudo apt-get -y install python3-dev python3-pip python3-numpy
 ```
 2. OpenCV
 - install
 ```
 $ cd ~
 
 $ wget -O opencv.zip https://github.com/opencv/opencv/archive/3.1.0.zip
 $ unzip opencv.zip
 
 $ wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.1.0.zip
 $ unzip opencv_contrib.zip
 
 $ cd opencv-3.1.0
 $ mkdir build
 $ cd build
 
 $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
         -D CMAKE_INSTALL_PREFIX=/usr/local \
         -D WITH_TBB=OFF \
         -D WITH_IPP=OFF \
         -D WITH_1394=OFF \
         -D BUILD_WITH_DEBUG_INFO=OFF \
         -D BUILD_DOCS=OFF \
         -D INSTALL_C_EXAMPLES=ON \
         -D INSTALL_PYTHON_EXAMPLES=ON \
         -D BUILD_EXAMPLES=OFF \
         -D BUILD_TESTS=OFF \
         -D BUILD_PERF_TESTS=OFF \
         -D WITH_QT=ON \
         -D WITH_OPENGL=ON \
         -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.1.0/modules \
         -D WITH_V4L=ON  \
         -D WITH_FFMPEG=ON \
         -D WITH_XINE=ON \
         -D BUILD_NEW_PYTHON_SUPPORT=ON ..
 
 $ time make
 $ sudo make install
 ```
 - import test
 ```
 $ python3
 >>> import cv2
 >>> cv2.__version__
 '3.1.0'
 >>> quit()
 ```
 3. Dlib
 - install
 ```
 $ cd ~
 
 $ sudo pip3 install dlib
 ```
 - import test
 ```
 $ python3
 >>> import dlib
 >>> dlib.__version__
 '19.10.0'
 >>> quit()
 ```
 4. Torch
 ```
 $ cd ~
 
 $ git clone https://github.com/torch/distro.git ~/torch --recursive
 
 It's not finished.
 ```
 
 5. Openface
 ```
 coming soon!
 ```
 
 6. Telepot
 - install
 ```
 $ cd ~
 
 $ sudo pip3 install telepot
 ```
 - import test
 ```
 $ python3
 >>> import telepot
 >>> telepot.__version__
 '12.6'
 >>> quit()
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
