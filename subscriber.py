import rospy
import publisher as pb
from std_msgs.msg import String
import tf2_ros
import tf2_msgs.msg

def callback(data): # logs info heard from listener
    # print(data.data)
    rospy.loginfo("Heard: %s", data.data)

def listener():
    #pb.talker()
    rospy.init_node('tf_listener')
    rospy.Subscriber("tf", tf2_msgs.msg.TFMessage, callback) # when data is received, parses data into callback classes
    rospy.spin()

if __name__ == '__main__':
    listener()
    # rospy.loginfo("Daniel is cute")
