import rclpy
from rclpy.node import Node
from std_msgs.msg import String          # 추가

class HelloNode(Node):
    def __init__(self):
        super().__init__('hello_node')
        self.publisher_ = self.create_publisher(String, 'hello_topic', 10)  # 추가
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = String()                   # 추가
        msg.data = 'Hello ROS2'          # 추가
        self.publisher_.publish(msg)     # 추가
        self.get_logger().info('Hello ROS2')

def main(args=None):
    rclpy.init(args=args)
    node = HelloNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()