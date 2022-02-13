import var
from networktables import NetworkTables

NetworkTables.initialize(server=var.ip)
table = NetworkTables.getTable("lidar")

def tf_data(trans, rot, dt):
    table.putNumber("p_x_pos", trans.x)
    table.putNumber("p_y_pos", trans.y)
    table.putNumber("p_heading", rot.z)
    table.putNumber("dt", dt)