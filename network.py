from networktables import NetworkTables

NetworkTables.initialize()
table = NetworkTables.getTable("lidar")

def send_data_to_table(trans, rot, dt):
    table.putNumber("p_x_pos", trans.x / rot.w)
    table.putNumber("p_y_pos", trans.y / rot.w)
    table.putNumber("p_heading", rot.x / rot.w)
    table.putNumber("dt", dt)
    

