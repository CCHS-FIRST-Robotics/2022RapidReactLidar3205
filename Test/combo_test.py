from networktables import NetworkTables
import time

NetworkTables.initialize()
table = NetworkTables.getTable("lidar")

while True:
    option = raw_input("1. DATA | 2. RESET...")
    if option == "1":
        print(table.getNumber("p_x_pos", -1))
        print(table.getNumber("p_y_pos", -1))
        print(table.getNumber("p_heading", -1))
        print(table.getNumber("dt", -1))
    elif option == "2":
        table.putBoolean("reset", True)
        time.sleep(1)
        table.putBoolean("reset", False)
    else:
        print("INVALID")