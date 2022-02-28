import tf
import rospy
import network as nw
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

def talk():
    odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)
    # odom_tf = tf.TransformBroadcaster()
    rospy.init_node('odom_talker', anonymous=True)

    old_vars = []
    while True:
        new_vars = nw.get_state() # x_pos, y_pos, heading, x_vel, y_vel, a_vel

        if new_vars != old_vars:
            current_time = rospy.Time.now()
            odom_quat = tf.transformations.quaternion_from_euler(0, 0, new_vars[2])

            # odom_tf.sendTransform(
            #     (x, y, 0.),
            #     odom_quat,
            #     current_time,
            #     "base_link",
            #     "odom"
            # )

            odom = Odometry()
            odom.child_frame_id = "base_link"
            
            odom.header.stamp = current_time
            odom.header.frame_id = "odom"

            odom.pose.pose = Pose(Point(new_vars[0], new_vars[1], 0.), Quaternion(*odom_quat))
            odom.twist.twist = Twist(Vector3(new_vars[3], new_vars[4], 0), Vector3(0, 0, new_vars[5]))

            odom_pub.publish(odom)
            new_vars = old_vars

if __name__ == "__main__":
    talk()