import rospy
import cartographer_ros_msgs.msg
import numpy

def callback(data):
    return 1

def listen():
    rospy.init_node('sub_map_listener')
    rospy.Subscriber("sub_map", cartographer_ros_msgs.msg.SubmapList, callback)  # when data is received, parses data into callback classes
    rospy.spin()
