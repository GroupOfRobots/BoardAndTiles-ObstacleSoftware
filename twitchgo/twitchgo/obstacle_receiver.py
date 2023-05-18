import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool

class Movement:
    pass

class Servomotor:
    pass

class MotorObstacleReceiver(Node):

    def __init__(self, obstacle_name: str):
        super().__init__(obstacle_name)
        self._obstacel_mover = Movement()
        self.subscription = self.create_subscription(Bool, f'{obstacle_name}_topic', self.listener_callback, 10)

    def listener_callback(self, msg: Bool):
        if msg.data:
            self._obstacel_mover.move_all(100, 100)
        else:
            self._obstacel_mover.stop()


class MotorObstacleReceiver(Node):

    def __init__(self, obstacle_name: str):
        super().__init__(obstacle_name)
        self._obstacel_mover = Servomotor()
        self.subscription = self.create_subscription(Bool, f'{obstacle_name}_topic', self.listener_callback, 10)

    def listener_callback(self, msg: Bool):
        if msg.data:
            self._obstacel_mover.moveUp()
        else:
            self._obstacel_mover.moveDown()
            

def main(args=None):
    pass


if __name__ == '__main__':
    main()