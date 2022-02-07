import rospy
import geometry_msgs.msg
import tf2_msgs.msg

def callback(data):
    rospy.loginfo(data.transforms[0].header)
    
if __name__ == "__main__":
    rospy.init_node("talker")
    rospy.Subscriber('tf', tf2_msgs.msg.TFMessage, callback)
    rospy.spin()