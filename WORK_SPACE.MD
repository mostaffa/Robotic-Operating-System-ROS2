# Create a Work Space

## Description
This document describes how to create a `ros2` work space in the system.

## Prerequisites
- `Ubuntu 22.04`
- `ROS2`
- `Humble`
- `Colcon`

## Procedure
1. Open the terminal.
2. Run the following command to create a workspace:
    ```bash
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws
    colcon build
    ```
3. Run the following command to source the workspace:
    ```bash
    source ~/ros2_ws/install/setup.bash
    ```
4. Run the following command to verify the workspace:
    ```bash
    echo $ROS_PACKAGE_PATH
    ```
5. The workspace is created successfully.
6. (Optional) add the following line to the `.bashrc` file:
    ```bash
    source ~/ros2_ws/install/setup.bash
    ```
    7. (Optional) add `colcon` bash path to the `.bashrc` file:
    ```bash
    source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
    # this will enable the colcon bash completion
    ```