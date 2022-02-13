from networktables import NetworkTables

ip = "127.0.0.1" # 10.32.5.2

NetworkTables.initialize(server=ip)
table = NetworkTables.getTable("lidar")

def tf_data(trans, rot, dt):
    table.putNumber("p_x_pos", trans.x)
    table.putNumber("p_y_pos", trans.y)
    table.putNumber("p_heading", rot.x)
    table.putNumber("dt", dt)

def get_reset():
    reset = table.getBoolean("reset", None)
    return reset
