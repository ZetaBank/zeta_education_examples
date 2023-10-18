cmake_minimum_required(VERSION 3.0.2)
project(my_socket_example)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS roscpp std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(server_node src/server_class.cpp)
target_link_libraries(server_node ${catkin_LIBRARIES})

add_executable(client_node src/client_class.cpp)
target_link_libraries(client_node ${catkin_LIBRARIES})
