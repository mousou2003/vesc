cmake_minimum_required(VERSION 2.8.3)
project(vesc-utils)
find_package(catkin REQUIRED)
catkin_package(
  CATKIN_DEPENDS
    rostopic
)
install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)