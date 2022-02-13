import os
import sys
import time
import rospy
import socket
import subprocess
from threading import Thread
from multiprocessing import Process

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
    tf_proc = Process(target=tf.listen)
    tf_proc.start()
    
    sm_proc = Process(target=sm.listen)
    sm_proc.start()
    
    return tf_proc, sm_proc
 
            
reset = False # Resets ROS if it receives True value over network tables

ros = ros_start()
tf_proc, sm_proc = proc_start()

while True:
    if not reset:
        if nt.get_reset():
            ros.terminate()
            ros.wait()
            
            tf_proc.terminate()
            sm_proc.terminate()
            
            ros = ros_start()
            tf_proc, sm_proc = proc_start()
            
            reset = True
    else:
        if not nt.get_reset():
            reset = False