import sys
import rospy
import pygame
from nav_msgs.msg import OccupancyGrid

pygame.init()

window_w = 800
window_h = 800

display = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("Point Cloud")

def callback(data):  # processes data heard from listener
    import map_test as mt
    
    # trans = data.transforms[1].transform.translation  # x and y translations in meters, z = 0
    # rot = data.transforms[1].transform.rotation  # z = rotation in radians/pi, w = constant
    # nsex = data.transforms[1].header.stamp.nsecs
    
    map_array = data.data
    
    width = data.info.width # Width of the map array
    height = data.info.height # Height of the... you know
    
    origin_x = round(data.info.origin.position.x)
    origin_y = round(data.info.origin.position.y)
    
    pygame_update(map_array, width, height, origin_x, origin_y)
    
    # Splits the 1D map array into seperate arrays based on the specified width and height provided by Cartographer
    # for y in range(height):
    #     map_row = []
    #     for x in range(width):
    #         map_row.append(map_array[y*width+x])
    #     print(map_row)
        
    # TODO: Do Tkinter or something to graph the points or something idk i'm tired    
        
    # print("---------------------")
    
def pygame_update(map_array, width, height, origin_x, origin_y):
    display.fill((0, 0, 0))
    
    for y in range(height):
        for x in range(width):
            color = map_array[y*width+x]
            display.set_at((origin_x + x, origin_y + y), pygame.Color(color, color, color))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
  
    pygame.display.update()
    

def listen():
    rospy.init_node('map_listener', anonymous=True)
    rospy.Subscriber("map", OccupancyGrid, callback)  # passes received data to callback method
    rospy.spin()


if __name__ == "__main__":
    listen()