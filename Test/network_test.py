from networktables import NetworkTables
import time

NetworkTables.initialize()
table = NetworkTables.getTable("lidar")

while True:
    print(table.getNumber("p_x_pos"))
    print(table.getNumber("p_y_pos"))
    print(table.getNumber("p_heading"))
    print(table.getNumber("dt"))
    time.sleep(1)