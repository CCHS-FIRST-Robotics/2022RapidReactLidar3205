import rospy
import cartographer_ros_msgs.msg
import pathfind as pf

def callback(data):
    pf.create_grid()

def listen():
    rospy.init_node('sub_map_listener')
    rospy.Subscriber("sub_map", cartographer_ros_msgs.msg.SubmapList, callback)  # when data is received, parses data into callback classes
    rospy.spin()
