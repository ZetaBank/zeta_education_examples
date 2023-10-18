#include <ros/ros.h>
#include <std_msgs/String.h>
#include <sstream>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "hello_Robot_fun_node");
  ros::NodeHandle nh;
  ros::Publisher chatter_pub = nh.advertise<std_msgs::String>("say_hello_Robot", 1000);
  ros::Rate loop_rate(10); // 0.1초마다 메시지를 보냅니다.
  int count = 0;

  while (ros::ok())
  {
    std_msgs::String msg;
    std::stringstream ss;

    if(count % 10 == 0) { // 1초마다
      ss << "This is a FUN message! Count: " << count;
    } else {
      ss << "안녕하세요 저희 로봇세계에 오신것을 환영합니다. " << count;
    }

    msg.data = ss.str();
    ROS_INFO("%s", msg.data.c_str());
    chatter_pub.publish(msg);

    ros::spinOnce();
    loop_rate.sleep();
    ++count;
  }

  return 0;
}
