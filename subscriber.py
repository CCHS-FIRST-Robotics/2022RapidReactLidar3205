import rospy
import tf2_msgs.msg
import network as nt
import vars

def callback(data):  # logs info heard from listener
    # print(data.data)
    trans = data.transforms[1].transform.translation  # X and Y are relative pos coords, z = 0
    rot = data.transforms[1].transform.rotation  # z = rotation in radians/pi ----- w = constant
    nsex = data.transforms[1].header.stamp.nsecs

    if vars.time_last_sent == 0:
        vars.time_last_sent = nsex

    dt = nsex - vars.time_last_sent

    nt.sendDataToTable(trans, rot, dt, nsex)
    vars.time_last_sent = nsex

def listen():
    rospy.init_node('tf_listener')
    rospy.Subscriber("tf", tf2_msgs.msg.TFMessage, callback) # when data is received, parses data into callback classes
    rospy.spin()



