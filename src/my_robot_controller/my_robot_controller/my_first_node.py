#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("first_node")
        self.get_logger().info("Hello From ROS2")

def main(args=None):
    rclpy.init(args=args)
    # Creating node
    node = MyNode()
    rclpy.spin(node=node) # keep node running
    rclpy.shutdown()

if __name__ == '__main__':
    main()