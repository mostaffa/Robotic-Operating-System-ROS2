#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class MoveArroundNode(Node):
    def __init__(self):
        super().__init__('move_arround')
        self.timer = 0.1
        self.cmd_vel_pub_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.timer_ = self.create_timer(self.timer, self.send_velocity)
        self.get_logger().info("Move Arround Node has been started")
        self.pose_ = None
        self.state = "Forward"
        self.avoid = {"direction": '', "duration": 0, "nextState": ""}

    def send_velocity(self):
        msg = Twist()
        if self.state == "Forward":
            msg.linear.x = 1.0
            msg.angular.z = 0.0
        elif self.state == "Stop":
            msg.linear.x = 0.0
            msg.angular.z = 0.0
        elif self.state == "Back":
            if self.avoid["duration"] <= 0:
                self.state = "Spin"
                self.avoid["duration"] = 1
            else:
                msg.linear.x = -1.0

            self.avoid["duration"] = self.avoid["duration"] - self.timer
        elif self.state == "Spin":
            if self.avoid["duration"] <= 0:
                self.state = "Forward"
                self.avoid["duration"] = 0
            else:
                if self.avoid["direction"] == "Left":
                    msg.angular.z = 1.0
                    # msg.linear.x = 0.5
                else:
                    msg.angular.z = -1.0
                    # msg.linear.x = 0.2
            self.avoid["duration"] = self.avoid["duration"] - self.timer
        print(self.avoid)
        self.cmd_vel_pub_.publish(msg)

    def pose_callback(self, msg):
        self.pose_ = msg
        if self.state != "Spin":
            if (self.pose_.x > 9) or (self.pose_.x < 1) or (self.pose_.y > 9) or (self.pose_.y < 1):
                self.state = "Back"
                self.avoid["direction"] = "Left"
                self.avoid["duration"] = self.timer
                self.avoid["nextState"] = "Spin"

def main(args=None):
    rclpy.init(args=args)
    node = MoveArroundNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()