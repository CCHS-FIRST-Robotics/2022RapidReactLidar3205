import rospy
import network as nw
from nav_msgs.msg import OccupancyGrid

def callback(data):
    map_array = data.data # Array of occupancy probabilities
    
    width = data.info.width # Width of the map array
    height = data.info.height # Height of the... you know
    
    origin_x = data.info.origin.position.x # Real world origin of map grid (0, 0)
    origin_y = data.info.origin.position.y

    nw.send_map_data(map_array, width, height, origin_x, origin_y)

def listen():
    rospy.init_node('map_listener', anonymous=True)
    rospy.Subscriber("map", OccupancyGrid, callback)  # passes received data to callback method
    rospy.spin()
    
if __name__ == "__main__":
    listen()