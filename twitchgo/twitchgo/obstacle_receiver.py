import rclpy
from rclpy.node import Node
import time
import datetime

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
            self.activate_obstacle()
        else:
            self._obstacel_mover.stop()
    
    def activate_obstacle(self):
        self._obstacel_mover.move_all(50, 50)
        time.sleep(20)
        #second way of waiting
        # start = time.time()
        # while time.time()-start < 20:
        #     pass
        self._obstacel_mover.stop()


class ServoObstacleReceiver(Node):

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
    rclpy.init(args=args)

    motor_receiver = MotorObstacleReceiver()

    rclpy.spin(motor_receiver)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    motor_receiver.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()