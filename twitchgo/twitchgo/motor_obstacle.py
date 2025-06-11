from rclpy.node import Node
from std_msgs.msg import Bool
from twitchgo.motor import Motor

class MotorObstacle(Node):
    def __init__(self, obstacle_name: str, topic_name:str, pwm_pin: int, first_in_pin: int, second_in_pin: int):
        super().__init__(f'{obstacle_name}_node')
        self._motor = Motor(pwm_pin, first_in_pin, second_in_pin)
        self.subscription = self.create_subscription(Bool, topic_name, self.listener_callback, 10)
        self.get_logger().info(f"Subscribed to {topic_name}")

    def listener_callback(self, msg: Bool):
        if msg.data:
            # random -1 or 1
            dir = 1 if self.get_clock().now().nanoseconds % 2 == 0 else -1
            self._motor.run(dir)  
            self.get_logger().info(f"Motor running in direction: {dir}")
        else:
            self._motor.stop()
            self.get_logger().info("Motor stopped")