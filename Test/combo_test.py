from networktables import NetworkTables
import time

NetworkTables.initialize()
table = NetworkTables.getTable("lidar")

print(table.getNumber("p_x_pos", -1))
print(table.getNumber("p_y_pos", -1))
print(table.getNumber("p_heading", -1))
print(table.getNumber("dt", -1))
time.sleep(1)
print(table.getNumber("p_x_pos", -1))
print(table.getNumber("p_y_pos", -1))
print(table.getNumber("p_heading", -1))
print(table.getNumber("dt", -1))
table.putBoolean("reset", True)
time.sleep(1)
table.putBoolean("reset", False)
time.sleep(5)
print(table.getNumber("p_x_pos", -1))
print(table.getNumber("p_y_pos", -1))
print(table.getNumber("p_heading", -1))
print(table.getNumber("dt", -1))