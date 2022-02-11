import rospy
import tf2_msgs.msg
import network as nt

time_last_sent = 0

def callback(data):  # processes data heard from listener
    import tf_handler as tf
    
    trans = data.transforms[1].transform.translation  # x and y translations in meters, z = 0
    rot = data.transforms[1].transform.rotation  # z = rotation in radians/pi, w = constant
    nsex = data.transforms[1].header.stamp.nsecs

    if tf.time_last_sent == 0:
        tf.time_last_sent = nsex

    dt = nsex - tf.time_last_sent

    nt.tf_data(trans, rot, dt)
    tf.time_last_sent = nsex

def listen():
    rospy.init_node('tf_listener')
    rospy.Subscriber("tf", tf2_msgs.msg.TFMessage, callback)  # passes received data to callback method
    rospy.spin()