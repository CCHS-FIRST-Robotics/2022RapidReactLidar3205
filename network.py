import var
from networktables import NetworkTables

# raspi radio IP - 10.32.5.19

NetworkTables.initialize(server=var.ip)

lidar = NetworkTables.getTable("lidar")
state = NetworkTables.getTable("State")
point = NetworkTables.getTable("point")

def send_tf_data(trans, rot, dt):
    lidar.putNumber("p_x_pos", trans.x)
    lidar.putNumber("p_y_pos", trans.y)
    lidar.putNumber("p_heading", rot.w) # rot.w is magnitude of the heading (z)
                                        # z decreases as the lidar rotates cw, increases as the lidar rotates cw' 
                                        # z, w = 0 at north
                                        # w magnitude of radians/pi
                                        # angle = {-w, z < 0}
                                        #         {w,  z > 0}
    lidar.putNumber("dt", dt)
    NetworkTables.flush()

def send_map_data(map_array, width, height, origin_x, origin_y):
    point.putNumberArray("m_array", map_array)
    point.putNumber("m_width", width)
    point.putNumber("m_height", height)
    point.putNumber("m_origin_x", origin_x)
    point.putNumber("m_origin_y", origin_y)
    NetworkTables.flush()

def get_reset():
    reset = lidar.getBoolean("reset", False)
    return reset

def get_state():
    vals = []

    vals.append(state.getNumber("x_pos", 0.0))
    vals.append(state.getNumber("y_pos", 0.0))
    vals.append(state.getNumber("heading", 0.0))
    vals.append(state.getNumber("x_vel", 0.0))
    vals.append(state.getNumber("y_vel", 0.0))
    vals.append(state.getNumber("a_vel", 0.0))

    return vals