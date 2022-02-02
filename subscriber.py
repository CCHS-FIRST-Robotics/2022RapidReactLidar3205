import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Heard: %s", data.data)

def listener():
    rospy.init_node('tf_listener')  # TODO: write node
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()
