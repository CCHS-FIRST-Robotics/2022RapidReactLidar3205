import rospy
import cartographer_ros_msgs.msg
import pathfind as pf

def callback(data):  # processes data heard from listener
    #pf.create_grid()
    pass

def listen():
    rospy.init_node('submap_listener')
    rospy.Subscriber("submap_list", cartographer_ros_msgs.msg.SubmapList, callback)  # passes received data to callback method
    rospy.spin()