from networktables import NetworkTables
import time

NetworkTables.initialize()
table = NetworkTables.getTable("lidar")

while True:
    input("PRESS ENTER")
    table.putBoolean("reset", True)
    time.sleep(1)
    table.putBoolean("reset", False)