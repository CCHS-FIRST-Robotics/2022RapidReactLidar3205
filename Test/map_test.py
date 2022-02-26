from itertools import tee
import rospy
from nav_msgs.msg import OccupancyGrid

def callback(data):  # processes data heard from listener
    # trans = data.transforms[1].transform.translation  # x and y translations in meters, z = 0
    # rot = data.transforms[1].transform.rotation  # z = rotation in radians/pi, w = constant
    # nsex = data.transforms[1].header.stamp.nsecs
    
    width = data.info.width # Width of the map array
    height = data.info.height # Height of the... you know
    
    map_array = data.data
    
    for y in range(height):
        map_row = []
        for x in range(width):
            map_row[x] = map_array[y*width+x]
        print(map_row)
        
    print("---------------------")
            
    
    

def listen():
    rospy.init_node('map_listener', anonymous=True)
    rospy.Subscriber("map", OccupancyGrid, callback)  # passes received data to callback method
    rospy.spin()


if __name__ == "__main__":
    listen()