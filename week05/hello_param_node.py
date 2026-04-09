import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloParamNode(Node):
    def __init__(self):
        super().__init__('hello_param_node')

        self.declare_parameter('interval', 1.0)
        interval = self.get_parameter('interval').get_parameter_value().double_value

        self.publisher_ = self.create_publisher(String, 'hello_topic', 10)
        self.timer = self.create_timer(interval, self.timer_callback)

        self.get_logger().info(f'interval: {interval}초')

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello ROS2'
        self.publisher_.publish(msg)
        self.get_logger().info('Hello ROS2')


def main(args=None):
    rclpy.init(args=args)
    node = HelloParamNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
