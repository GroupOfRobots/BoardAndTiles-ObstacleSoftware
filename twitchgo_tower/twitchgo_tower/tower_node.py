from rclpy.node import Node
from std_msgs.msg import Bool
from twitchgo_tower.servo_motor import ServoMotor

HORIZONTAL_SERVO_PIN = 19
VERTICAL_SERVO_PIN = 12

class TowerNode(Node):
    def __init__(self):
        super().__init__()
        self.horizontal_servo = ServoMotor(HORIZONTAL_SERVO_PIN)
        self.vertical_servo = ServoMotor(VERTICAL_SERVO_PIN)
        self.topic_name = 'tower_move'
        self.subscription = self.create_subscription(Bool, self.topic_name, self.listener_callback, 10)
        self.get_logger().info(f"Subscribed to {self.topic_name}")
        
    def listener_callback(self, msg: Bool):
        if msg.data:
            self.get_logger().info("Moving tower to random position")
            self.horizontal_servo.move_to_random_position()

            self.vertical_servo.move_to_random_extreme()
            self.vertical_servo.move_to_mid_position()