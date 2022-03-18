import tf
import rospy
import network as nw
from math import sin, cos, pi
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

def talk():
    rate = rospy.Rate(10)

    last_vars = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    odom_lock = True

    # Creates odom topic when network tables are initialized
    while odom_lock: 
        if nw.get_state != last_vars:
            odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)
            # odom_tf = tf.TransformBroadcaster()
            rospy.init_node('odom_talker', anonymous=True)
            odom_lock = False

            rate.sleep()

    x = 0.0
    y = 0.0
    th = 0.0

    current_time = rospy.Time.now()
    last_time = rospy.Time.now()

    while True:
        current_vars = nw.get_state() # x_pos (0), y_pos (1), heading (2), x_vel (3), y_vel (4), a_vel (5)

        if current_vars != last_vars:
            x_pos  = current_vars[0]
            y_pos  = current_vars[1]
            th_pos = current_vars[2]
            x_vel  = current_vars[3]
            y_vel  = current_vars[4]
            a_vel  = current_vars[5]

            current_time = rospy.Time.now()
            dt = (current_time - last_time).to_sec()

            delta_x = (x_vel * cos(th_pos) - y_vel * sin(th_pos)) * dt
            delta_y = (x_vel * sin(th_pos) + y_vel * cos(th_pos)) * dt
            delta_th = a_vel * dt

            x += delta_x
            y += delta_y
            th += delta_th

            odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)

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

            odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))
            odom.twist.twist = Twist(Vector3(x_vel, y_vel, 0), Vector3(0, 0, a_vel))

            odom_pub.publish(odom)
            current_vars = last_vars

            rate.sleep()

if __name__ == "__main__":
    talk()