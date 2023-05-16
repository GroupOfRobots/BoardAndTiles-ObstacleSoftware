import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool


class ObstacleActivator(Node):

    def __init__(self, obstacle_name: str, control_method):
        super().__init__(obstacle_name)
        self._control_method = control_method
        self.subscription = self.create_subscription(Bool, f'{obstacle_name}_topic', self.listener_callback, 10)

    def listener_callback(self, msg: Bool):
        self._control_method(msg.data)


def main(args=None):
    pass
    # rclpy.init(args=args)

    # minimal_publisher = MinimalPublisher()

    # rclpy.spin(minimal_publisher)

    # # Destroy the node explicitly
    # # (optional - otherwise it will be done automatically
    # # when the garbage collector destroys the node object)
    # minimal_publisher.destroy_node()
    # rclpy.shutdown()


if __name__ == '__main__':
    main()