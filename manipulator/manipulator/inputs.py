import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math

class JointStatePublisher(Node):

    def __init__(self):
        super().__init__('joint_state_publisher')
        self.publisher_ = self.create_publisher(JointState, '/joint_commands', 10)
        self.timer_ = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info('Joint State Publisher Node started')
        self.time_ = 0

    def timer_callback(self):
        msg = JointState()
        msg.header.stamp.sec = 0
        msg.header.stamp.nanosec = 0
        msg.header.frame_id = 'frame_id'
        msg.name = ['joint_1', 'joint_2']

        # Calculate sine wave positions based on current time
        position_1 = math.sin(self.time_ / 100)
        position_2 = math.sin(self.time_ / 100)

        msg.position = [position_1, position_2]

        self.publisher_.publish(msg)
        self.get_logger().info('Published joint state command: [%f, %f]' % (position_1, position_2))

        self.time_ += 1

def main(args=None):
    rclpy.init(args=args)

    joint_state_publisher = JointStatePublisher()

    rclpy.spin(joint_state_publisher)

    joint_state_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
