import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
from typing import List


class ObstacleActivator(Node):

    def __init__(self, obstacle_names: List[str]):
        super().__init__("Obstacles")
        self._obstacles_pub = {}
        for obstac in obstacle_names:
            self._obstacles_pub[obstac] = self.create_publisher(Bool, f'{obstac}_topic', 10)
    def start_obstacle(self, obstsacle_name: str):
        msg = Bool()
        msg.data = True
        self._publish_message(msg, obstsacle_name)

    def stop__obstacle(self, obstsacle_name: str):
        msg = Bool()
        msg.data = False
        self._publish_message(msg, obstsacle_name)

    def _publish_message(self, msg: Bool, obstsacle_name: str):
        self._obstacles_pub[obstsacle_name].publish(msg)
        

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = ObstacleActivator(["adx", "jjj"])

    # rclpy.spin(minimal_publisher)
    while True:
        minimal_publisher.start_obstacle("adx")
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()