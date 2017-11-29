#!/bin/bash

source /opt/ros/indigo/setup.bash
source ~/ros_ws/devel/setup.bash
export TURTLEBOT_3D_SENSOR=kinect

# ONEMLI NOT: ASAGIDAKI launch.py ve app.py BELGELERININ BULUNDUGU DIZINLER DUZELTILMELIDIR. 

python /home/kahya/Desktop/INTROBOT/src/launch.py & python /home/kahya/Desktop/INTROBOT/src/app.py
