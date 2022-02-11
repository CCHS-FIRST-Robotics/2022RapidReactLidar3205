import os
import multiprocessing as mp
import network as nt
import tf_handler as tf
import submap_handler as sm

path = "~/catkin_ws"

def reset_ros():
    os.system(". " + path + "/devel/setup.sh && roslaunch gbot_core gbot.launch")

reset = False # Resets ROS if it receives True value over network tables
proc = mp.Process(target=reset_ros)
proc.start()

while True:
    if not reset:
        if nt.get_reset():
            proc.kill()
            proc.close()
            proc.start()
            reset = True
    else:
        if not nt.get_reset():
            reset = False

    tf.listen()
    sm.listen()