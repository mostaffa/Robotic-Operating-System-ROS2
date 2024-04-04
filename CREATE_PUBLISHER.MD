# Create a Publisher

In this tutorial, we will create a publisher node that publishes a message to a topic. The publisher node will publish a message of type `std_msgs::msg::Twist` to the topic `turtlesim`.

## Step 1: Create a publisher node

First, create a new file called `draw_circle.py` in the `src/my_robot_controller/my_robot_controller` directory of your package. Add the following code to the file:

```python
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist # should be added also in the package.xml <depend>geometry_msgs</depend>

class DrawCircle(Node):
    def __init__(self):
        super().__init__('draw_circle')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        # topic name is '/turtle1/cmd_vel' and message type is Twist, should be added also in the package.xml <depend>turtlesim</depend>
        self.timer = self.create_timer(0.5, self.publish_message)

    def publish_message(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```

This code creates a publisher node that publishes a message of type `std_msgs::msg::Twist` to the topic `turtlesim`. The message contains linear and angular velocities that will make the turtle in the `turtlesim` simulator draw a circle.

