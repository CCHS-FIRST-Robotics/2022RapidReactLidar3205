import tf
import rospy
import network as nw
from math import sin, cos, pi
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3, TransformStamped


def talk():
    last_vars = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    odom_lock = True

    # Creates odom topic when network tables are initialized
    while odom_lock: 
        if nw.get_state() != last_vars:
            odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)
            # odom_tf = tf.TransformBroadcaster()
            rospy.init_node('odom_talker', anonymous=True)
            odom_lock = False

    current_time = rospy.Time.now()
    last_time = rospy.Time.now()

    rate = rospy.Rate(100) # in 1/s, TODO: change when optimal rate is determined

    while not rospy.is_shutdown():
        current_vars = nw.get_state() # x_pos (0), y_pos (1), heading (2), x_vel (3), y_vel (4), a_vel (5)

        if current_vars != last_vars:
            x_pos  = current_vars[0]
            y_pos  = current_vars[1]
            heading = current_vars[2]
            x_vel  = current_vars[3]
            y_vel  = current_vars[4]
            a_vel  = current_vars[5]

            current_time = rospy.Time.now()
            dt = (current_time - last_time).to_sec()

            odom_quat = tf.transformations.quaternion_from_euler(0, 0, heading) # use th, or use heading?

            odom_trans = TransformStamped()
            odom_trans.header.stamp = current_time
            odom_trans.header.frame_id = "odom"
            odom_trans.child_frame_id = "base_link"

            odom_br = tf.TransformBroadcaster()

            odom_trans.transform.translation.x = x_pos
            print(odom_trans.transform.translation.x) # testing if able to set values like this
            odom_trans.transform.translation.y = y_pos
            odom_trans.transform.translation.z = 0.0
            odom_trans.transform.rotation = odom_quat

            odom_br.sendTransform(odom_trans)

            odom = Odometry()
            odom.header.stamp = current_time
            odom.header.frame_id = "odom"

            odom.pose.pose.position.x = x_pos
            odom.pose.pose.position.y = y_pos
            odom.pose.pose.position.z = 0.0
            odom.pose.pose.orientation = odom_quat

            odom.child_frame_id = "base_link"
            odom.twist.twist.linear.x = x_vel
            odom.twist.twist.linear.y = y_vel
            odom.twist.twist.angular.z = a_vel

            odom_pub.publish(odom)

            list_time = current_time
            current_vars = last_vars

if __name__ == "__main__":
    talk()