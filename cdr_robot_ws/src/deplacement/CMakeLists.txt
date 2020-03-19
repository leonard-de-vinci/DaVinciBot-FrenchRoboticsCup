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
  dynamic_reconfigure
)

FIND_LIBRARY(WIRINGPI_LIBRARY wiringPi /home/gab/wiringPi)
# find_package(dvb_hardware REQUIRED)

generate_dynamic_reconfigure_options(cfg/Robot.cfg)  

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
  # ${dvb_hardware_INCLUDE_DIRS}
)

include_directories(${dynamic_reconfigure_PACKAGE_PATH}/cmake/cfgbuild.cmake) 

LINK_DIRECTORIES("/usr/local/lib")

#add_executable(deplacement src/deplacement.cpp)
#target_link_libraries(deplacement ${CATKIN_LIBRARIES} ${WIRINGPI_LIBRARY})

add_executable(depart  src/depart.cpp)
target_link_libraries(depart ${CATKIN_LIBRARIES} ${WIRINGPI_LIBRARY})

#add_executable(drapeau  src/drapeau.cpp)
#target_link_libraries(drapeau ${CATKIN_LIBRARIES} ${WIRINGPI_LIBRARY})

#add_executable(nodenulle src/nodenulle.cpp)
#target_link_libraries(nodenulle ${CATKIN_LIBRARIES} ${WIRINGPI_LIBRARY})

#add_executable(tets src/tets.cpp)
#target_link_libraries(tets ${CATKIN_LIBRARIES} ${WIRINGPI_LIBRARY})

# add_executable(Control src/Control.cpp)
# add_dependencies(Control ${PROJECT_NAME}_gencfg)
# target_link_libraries(Control 
#    ${catkin_LIBRARIES}
# )

#target_link_libraries(deplacement
#   ${catkin_LIBRARIES}
#)

target_link_libraries(depart
   ${catkin_LIBRARIES}
)

#target_link_libraries(drapeau
#   ${catkin_LIBRARIES}
#)

#target_link_libraries(nodenulle
#   ${catkin_LIBRARIES}
#)

#target_link_libraries(tets
#   ${catkin_LIBRARIES}
#)