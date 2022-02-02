import rospy
import tf
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Heard: %s", data.data)

def listener():
    rospy.init_node('tf_listener')  # TODO: write node
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()

if __name__ == '__main__'
    rate = rospy.Rate(10.0)
    listener = tf.TransformListener()
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform('/turtle2', '/turtle1', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

    print(trans)
    print(rot)
