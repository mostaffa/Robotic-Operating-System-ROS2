# Create a node
## Description
This document describes how to create a `ros2` node in the system.

## Prerequisites
- `Ubuntu 22.04`
- `ROS2`
- `Humble`
- `Colcon`
- `ros2_ws` workspace

## Procedure
1. Open the terminal.
2. Run the following command to create a node:
    ```bash
    cd ~/ros2_ws/src/my_robot_controller/my_robot_controller
    touch my_first_node.py
    ```
    ```python
    #!/usr/bin/env python3
    import rclpy # ROS Client Library for Python
    from rclpy.node import Node # Node class

    class MyFirstNode(Node):
        def __init__(self):
            super().__init__('my_first_node')
            self.get_logger().info('Hello ROS2')

    def main(args=None):
        rclpy.init(args=args) # initialize the ROS client library
        node = MyFirstNode() # create an instance of the node
        rclpy.spin(node) # keep the node running
        rclpy.shutdown() # shutdown the ROS client library

    if __name__ == '__main__':
        main()
    ```
    3. In `setup.py` file, add the following line:
    ```python
    entry_points={
        'console_scripts': [
            'test_node = my_robot_controller.my_first_node:main'
        ],
    },
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
4. Run the following command to source the workspace:
    ```bash
    source ~/ros2_ws/install/setup.bash
    ```
5. Run the following command to run the node:
    ```bash
    ros2 run my_robot_controller test_node
    ```
6. The node is created successfully.

