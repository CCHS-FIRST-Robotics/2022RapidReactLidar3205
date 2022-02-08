import rospy
import tf2_msgs.msg
import network as nt

time_last_sent = 0

def callback(data):  # logs info heard from listener
    import subscriber as sb # callback function is isolated so this is necessary to access some variables

    trans = data.transforms[1].transform.translation  # X and Y are relative pos coords, z = 0
    rot = data.transforms[1].transform.rotation  # z = rotation in radians/pi ----- w = constant
    sex = data.transforms[1].header.stamp.secs

    if sb.time_last_sent == 0:
        sb.time_last_sent = sex
    dt = sex - sb.time_last_sent

    nt.send_data_to_table(trans, rot, dt)
    sb.time_last_sent = sex

def listen():
    rospy.init_node('tf_listener')
    rospy.Subscriber("tf", tf2_msgs.msg.TFMessage, callback) # when data is received, parses data into callback classes
    rospy.spin()

if __name__ == '__main__':
    listener()

