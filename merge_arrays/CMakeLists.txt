cmake_minimum_required(VERSION 3.5)
project(merge_arrays)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(merge_arrays_node scripts/merge_arrays_node.py)

ament_target_dependencies(merge_arrays_node rclpy std_msgs)

install(TARGETS
  merge_arrays_node
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/merge_arrays_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()

