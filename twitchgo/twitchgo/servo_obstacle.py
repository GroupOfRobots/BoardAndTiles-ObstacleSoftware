from rclpy.node import Node
from std_msgs.msg import Bool
from twitchgo.servo_motor import ServoMotor

class ServoObstacle(Node):
    def __init__(self, obstacle_name: str, topic_name:str,  pwm_pin: int):
        super().__init__(obstacle_name)
        self._obstacle_mover = ServoMotor(pwm_pin)
        self.subscription = self.create_subscription(Bool, topic_name, self.listener_callback, 10)
        self.get_logger().info(f"Subscribed to {topic_name}")
        
    def listener_callback(self, msg: Bool):
        if msg.data:
            self._obstacle_mover.moveUp()
        else:
            self._obstacle_mover.moveDown()
