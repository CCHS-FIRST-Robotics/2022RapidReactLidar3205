import os
import rospy
import subprocess
from threading import Thread

import network as nt
import tf_handler as tf
import submap_handler as sm

path = "~/catkin_ws" # TEMP PATH

reset = False # Resets ROS if it receives True value over network tables
ros = subprocess.Popen([". " + path + "/devel/setup.sh && roslaunch gbot_core gbot.launch"], shell=True)
rospy.init_node('node')

while True:
    if not reset:
        if nt.get_reset():
            ros.kill()
            ros = subprocess.Popen([". " + path + "/devel/setup.sh && roslaunch gbot_core gbot.launch"], shell=True)
            reset = True
    else:
        if not nt.get_reset():
            reset = False
    
    tf.listen()
    sm.listen()