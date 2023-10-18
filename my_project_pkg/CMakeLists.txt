cmake_minimum_required(VERSION 2.8.3)
project(my_project_pkg)
find_package(catkin REQUIRED COMPONENTS roscpp std_msgs)
catkin_package(CATKIN_DEPENDS roscpp std_msgs)
include_directories(${catkin_INCLUDE_DIRS})
add_executable(hello_world_node src/hello_world_node.cpp)
target_link_libraries(hello_world_node ${catkin_LIBRARIES})

add_executable(My_name src/My_name.cpp)
target_link_libraries(My_name ${catkin_LIBRARIES})

add_executable(My_Project src/My_Project.cpp)
target_link_libraries(My_Project ${catkin_LIBRARIES})
