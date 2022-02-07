import rospy
import publisher as pb
from std_msgs.msg import String

def callback(data): # logs info heard from listener
 #   print(data.data)
    print("data should precede this line")
    rospy.loginfo("Heard: %s", data.data)

def listener():
    pb.talker()
#    rospy.init_node('listener', anonymous=True)
    print("Daniel face")
    rospy.Subscriber("chatter", String, callback) # when data is received, parses data into callback classes
    print("daniel face 2")
    rospy.spin()

if __name__ == '__main__':
    listener()
    # rospy.loginfo("Daniel is cute")
