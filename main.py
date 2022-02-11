import os
import rospy
import multiprocessing as mp
import network as nt
import tf_handler as tf
import submap_handler as sm

path = "~/Desktop/Lidar" # TEMP PATH

def reset_ros():
    os.system(". " + path + "/devel/setup.sh && roslaunch gbot_core gbot.launch")

rospy.init_node('node', anonymous=True)

reset = False # Resets ROS if it receives True value over network tables
ros = mp.Process(target=reset_ros)
ros.start()

tf = mp.Process(target=tf.listen)
tf.start()

sm = mp.Process(target=sm.listen)
sm.start()

while True:
    if not reset:
        if nt.get_reset():
            ros.kill()
            ros.close()
            ros.start()
            reset = True
    else:
        if not nt.get_reset():
            reset = False

    