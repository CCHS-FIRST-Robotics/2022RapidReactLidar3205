import var
import rospy
import subprocess
import network as nw
from roslaunch.parent import ROSLaunchParent


def ros_start(): # Starts and waits for ROS to initialize
    ros = ROSLaunchParent("ros", [var.path + '/src/gbot_core/launch/gbot.launch'])
    ros.start()
            
    rospy.sleep(5)
    return ros
 
    
def proc_start():
    tf_proc = subprocess.Popen(['python', 'tf_handler.py'])
    od_proc = subprocess.Popen(['python', 'odom_handler.py'])
    
    return tf_proc, od_proc


reset = False # Resets ROS if it receives True value over network tables
ros = ros_start()
tf_proc, od_proc = proc_start()

while True:
    if not reset:
        if nw.get_reset():
            ros.shutdown()
            
            tf_proc.terminate()
            tf_proc.wait()
            od_proc.kill() # Bad practice?
            od_proc.wait()
            
            ros = ros_start()
            tf_proc, od_proc = proc_start()
            
            reset = True
    else:
        if not nw.get_reset():
            reset = False