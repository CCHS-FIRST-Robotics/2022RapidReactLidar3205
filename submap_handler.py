import rospy
import cartographer_ros_msgs.msg
import pathfind as pf

def callback(data):  # processes data heard from listener
    pf.create_grid()

def listen():
    rospy.Subscriber("submap_list", cartographer_ros_msgs.msg.SubmapList, callback)  # passes received data to callback method