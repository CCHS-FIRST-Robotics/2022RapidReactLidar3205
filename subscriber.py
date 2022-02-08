import rospy
import publisher as pb
from std_msgs.msg import String
import tf2_ros
import tf2_msgs.msg
import network as nt

index = 0
time_last_sent = 0
def callback(data):  # logs info heard from listener
    # print(data.data)
    trans = data.transforms[1].transform.translation  # X and Y are relative pos coords, z = 0
    rot = data.transforms[1].transform.rotation  # z = rotation in radians/pi ----- w = constant
    sex = data.transforms[1].header.stamp.secs

    if index == 0:
        time_last_sent = sex
        index = 1
    dt = sex - time_last_sent

    nt.sendDataToTable(trans, rot, dt, sex)

    rospy.loginfo("------------------")

    rospy.loginfo("translation: ")
    rospy.loginfo(trans)

    rospy.loginfo("rotation: ")
    rospy.loginfo(rot)

    time_last_sent = sex

def listen():
    rospy.init_node('tf_listener')
    rospy.Subscriber("tf", tf2_msgs.msg.TFMessage, callback) # when data is received, parses data into callback classes
    rospy.spin()

if __name__ == '__main__':
    listener()

