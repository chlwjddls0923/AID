from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hello_pkg',
            executable='hello_param_node',
            name='hello_param_node',
            parameters=[{'interval': 0.5}]
        )
    ])
