cmake_minimum_required(VERSION 2.8.3)
project(deplacement)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  nav_msgs
  roscpp
  rospy
  std_msgs
  sensor_msgs
)

FIND_LIBRARY(WIRINGPI_LIBRARY wiringPi /home/gab/wiringPi)
find_package(dvb_hardware REQUIRED)


###################################
## catkin specific configuration ##
###################################
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES motor_controller
#  CATKIN_DEPENDS roscpp
#  DEPENDS system_lib
)

###########
## Build ##
###########

include_directories(
 include
  ${catkin_INCLUDE_DIRS}
  ${dvb_hardware_INCLUDE_DIRS}
)

LINK_DIRECTORIES("/usr/local/lib")

add_executable(deplacement src/deplacement.cpp)
target_link_libraries(deplacement ${CATKIN_LIBRARIES} ${WIRINGPI_LIBRARY})

add_executable(depart  src/depart.cpp)
target_link_libraries(depart ${CATKIN_LIBRARIES} ${WIRINGPI_LIBRARY})

add_executable(drapeau  src/drapeau.cpp)
target_link_libraries(drapeau ${CATKIN_LIBRARIES} ${WIRINGPI_LIBRARY})

add_executable(nodenulle src/nodenulle.cpp)
target_link_libraries(nodenulle ${CATKIN_LIBRARIES} ${WIRINGPI_LIBRARY})

target_link_libraries(deplacement
   dvb_map
   dvb_robot
   dvb_hardware
   ${catkin_LIBRARIES}
)

target_link_libraries(depart
   dvb_map
   dvb_robot
   dvb_hardware
   ${catkin_LIBRARIES}
)

target_link_libraries(drapeau
   dvb_map
   dvb_robot
   dvb_hardware
   ${catkin_LIBRARIES}
)

target_link_libraries(nodenulle
   dvb_map
   dvb_robot
   dvb_hardware
   ${catkin_LIBRARIES}
)
