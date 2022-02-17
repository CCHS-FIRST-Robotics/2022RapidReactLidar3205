import var
from networktables import NetworkTables

# raspi radio IP - 10.32.5.19

NetworkTables.initialize(server=var.ip)

lidar = NetworkTables.getTable("lidar")
state = NetworkTables.getTable("State")

def tf_data(trans, rot, dt):
    lidar.putNumber("p_x_pos", trans.x)
    lidar.putNumber("p_y_pos", trans.y)
    lidar.putNumber("p_heading", rot.w) # rot.w is the position of the point the lidar in rotating around
                                        # z decreases as the lidar rotates cw, increases as the lidar rotates cw'
                                        # w = |radians/pi|
                                        # angle = {-w, z < 0}
                                        #         {w,  z > 0}
    lidar.putNumber("dt", dt)
    
def get_reset():
    reset = lidar.getBoolean("reset", False)
    return reset

def get_state():
    vals = []

    vals.append(state.getNumber("x_pos", 0.0))
    vals.apeend(state.getNumber("y_pos", 0.0))
    vals.append(state.getNumber("heading", 0.0))
    vals.append(state.getNumber("x_vel", 0.0))
    vals.append(state.getNumber("y_vel", 0.0))
    vals.append(state.getNumber("a_vel", 0.0))

    return vals