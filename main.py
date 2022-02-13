import os
import sys
import time
import rospy
import socket
import subprocess

import network as nt
import tf_handler as tf
import submap_handler as sm

path = "~/catkin_ws" # TEMP PATH


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def ros_start(): # Waits for ROS nodes to start before reading from topics
    ros = subprocess.Popen([". " + path + "/devel/setup.sh && exec roslaunch gbot_core gbot.launch"], shell=True)
    online = False
    
    while not online:
        if sock.connect_ex(('127.0.0.1', 11311)) == 0:
            online = True
        else:
            time.sleep(1)
        
    time.sleep(5) # BRUTE FORCE SLEEP MAY BREAK IN SOME CASES
    return ros
 
    
def proc_start():
    tf_proc = subprocess.Popen(['python', 'tf_handler.py'])
    sm_proc = subprocess.Popen(['python', 'submap_handler.py'])
    
    return tf_proc, sm_proc
 
            
reset = False # Resets ROS if it receives True value over network tables

ros = ros_start()
tf_proc, sm_proc = proc_start()

while True:
    if not reset:
        if nt.get_reset():
            ros.terminate()
            tf_proc.terminate()
            sm_proc.terminate()
            
            ros.wait()
            tf_proc.wait()
            sm_proc.wait()
            
            ros = ros_start()
            tf_proc, sm_proc = proc_start()
            
            reset = True
    else:
        if not nt.get_reset():
            reset = False