import rospy
import network as nw
from tf2_msgs.msg import TFMessage

time_last_sent = 0

def callback(data):  # processes data heard from listener
    import tf_handler as tf
    
    trans = data.transforms[1].transform.translation  # x and y translations in meters, z = 0
    rot = data.transforms[1].transform.rotation  # z = rotation in radians/pi, w = constant
    nsex = data.transforms[1].header.stamp.nsecs

    if tf.time_last_sent == 0:
        tf.time_last_sent = nsex

    dt = nsex - tf.time_last_sent

    nw.send_tf_data(trans, rot, dt)
    tf.time_last_sent = nsex

def listen():
    rospy.init_node('tf_listener', anonymous=True)
    rospy.Subscriber("tf", TFMessage, callback)  # passes received data to callback method
    rospy.spin()
    
if __name__ == "__main__":
    listen()