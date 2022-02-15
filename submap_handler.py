import rospy
import pathfind as pf
from cartographer_ros_msgs.msg import SubmapList

def callback(data):  # processes data heard from listener
    #pf.create_grid()
    pass

def listen():
    rospy.init_node('submap_listener')
    rospy.Subscriber("submap_list", SubmapList, callback)  # passes received data to callback method
    rospy.spin()
    
if __name__ == "__main__":
    listen()