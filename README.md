# rpLidar

Important Articles:

  TF:

    http://wiki.ros.org/navigation/Tutorials/RobotSetup/TF

    https://web.ics.purdue.edu/~rvoyles/Classes/ROSprogramming/Lectures/TF%20(transform)%20in%20ROS.pdf

    http://docs.ros.org/en/diamondback/api/tf2_msgs/html/msg/TFMessage.html 
    
  submap_list:
  
    https://github.com/cartographer-project/cartographer_ros/blob/master/cartographer_ros_msgs/msg/SubmapList.msg
    
    https://github.com/cartographer-project/cartographer_ros/blob/master/cartographer_ros_msgs/msg/SubmapEntry.msg
    
  Odometry:
  
    http://wiki.ros.org/tf2/Tutorials/Quaternions
    
    https://answers.ros.org/question/346720/set-xy-goals-and-move-the-robot/
    
    https://www.miguelalonsojr.com/blog/robotics/ros/python3/2019/08/20/ros-melodic-python-3-build.html


Notes:

    nav_msgs/Odometry Message

    Pose

      Expresses “pose” composed of position and orientation

        Point position —> (x,y) position
        Quaternion orientation —> (z,w) rotation orientation
        
    Twist

      Expresses velocity broken into its linear and angular parts

        Vector3 linear —> linear velocity
        Vector3 angular —> angular velocity
