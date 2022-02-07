import rospy
import publisher as pb
from std_msgs.msg import String
import tf2_ros
import tf2_msgs.msg

translationsXYZ = [] # X and Y are relative pos coords, z = 0
rotationsXYZW = [] # z = rotation in radians/pi ----- w = constant

def callback(data): # logs info heard from listener
    # print(data.data)
    trans = data.transforms[0].transform.translation
    rot = data.transforms[0].transform.rotation
    translationsXYZ.append(trans)
    rotationsXYZW.append(rot)

    rospy.loginfo("------------------")

    rospy.loginfo("translation: ")
    rospy.loginfo(trans)

    rospy.loginfo("rotation: ")
    rospy.loginfo(rot)


def listener():
    #pb.talker()
    rospy.init_node('tf_listener')
    rospy.Subscriber("tf", tf2_msgs.msg.TFMessage, callback) # when data is received, parses data into callback classes
    rospy.spin()

if __name__ == '__main__':
    listener()
    # rospy.loginfo("Daniel is cute")
