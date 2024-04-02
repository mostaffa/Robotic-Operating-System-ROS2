# Create a Package

## Description
This document describes how to create a `ros2` package in the system.

## Prerequisites
- `Ubuntu 22.04`
- `ROS2`
- `Humble`
- `Colcon`

## Procedure
1. Open the terminal.
2. Run the following command to create a package:
    ```bash
    cd ~/ros2_ws/src
    # for python build type:
    ros2 pkg create --build-type ament_python my_robot_controller
    # for cpp build type:
    ros2 pkg create --build-type ament_cmake my_robot_controller
    ```
3. Run the following command to build the workspace:
    ```bash
    cd ~/ros2_ws
    colcon build
    # Expected output:
    # Starting >>> my_robot_controller
    # Finished <<< my_robot_controller [1.0s]
    # Summary: 1 package finished [1.1s]
    ```