import os
import var
import time
import rospy
import signal
import socket
import subprocess
import network as nw
from networktables import NetworkTables


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def ros_start(): # Waits for ROS to start
    ros = ROSLaunchParent("ros", [var.path + '/src/gbot_core/launch/gbot.launch'])
    ros.start()
            
    rospy.sleep(5) # BRUTE FORCE SLEEP MAY BREAK IN SOME CASES
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
        if nw.get_reset():
            ros.shutdown()
            rospy.sleep(5)
            
            tf_proc.terminate()
            tf_proc.wait()
            sm_proc.terminate()
            sm_proc.wait()
            
            ros = ros_start()
            tf_proc, sm_proc = proc_start()
            
            reset = True
    else:
        if not nw.get_reset():
            reset = False