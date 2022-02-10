import subprocess
import network as nt
import tf_handler as tf
import submap_handler as sm

reset = False # Resets ROS if it receives True value over network tables
ros = subprocess.Popen(["roslaunch gbot_core gbot.launch"])

while True:
    if not reset:
        if nt.get_reset():
            ros.terminate()
            ros = subprocess.Popen(["roslaunch gbot_core gbot.launch"])
            
            reset = True
    else:
        if not nt.get_reset():
            reset = False

    tf.listen()
    sm.listen()