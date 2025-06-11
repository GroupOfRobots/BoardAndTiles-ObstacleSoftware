from rclpy.node import Node
from std_msgs.msg import Bool
from twitchgo.motor import Motor

class MotorObstacle(Node):
    def __init__(self, obstacle_name: str, pwm_pin: int, first_in_pin: int, second_in_pin: int):
        super().__init__(obstacle_name)
        self._motor = Motor(pwm_pin, first_in_pin, second_in_pin)
        self.subscription = self.create_subscription(Bool, obstacle_name, self.listener_callback, 10)

    def listener_callback(self, msg: Bool):
        if msg.data:
            self._motor.run(TODO)  
        else:
            self._motor.stop()
    

