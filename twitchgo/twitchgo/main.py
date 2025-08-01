import rclpy
from twitchgo.servo_obstacle import ServoObstacle
from twitchgo.motor_obstacle import MotorObstacle
from ament_index_python.packages import get_package_share_directory
from rclpy.executors import MultiThreadedExecutor
import os
import yaml

def get_obstacles_from_config():
    package_share_directory = get_package_share_directory('twitchgo')
    yaml_file_path = os.path.join(package_share_directory, 'resource', 'traps.yaml')
    with open(yaml_file_path, 'r') as file:
        config = yaml.safe_load(file)
        return config.get('traps', [])
    
def main(args=None):
    rclpy.init(args=args)
    
    nodes = []

    for trap in get_obstacles_from_config():
        config = trap.get('config', {})

        if config['type'] == 'motor':
            nodes.append(MotorObstacle(trap['name'], trap['ros_topic'], config['pwm_pin'], config['forward_pin'], config['backward_pin']))
        elif config['type'] == 'servo':
            nodes.append(ServoObstacle(trap['name'], trap['ros_topic'], config['pwm_pin']))


    executor = MultiThreadedExecutor()
    for node in nodes:
        executor.add_node(node)
    
    try:
        executor.spin()
    finally:
        for node in nodes:
            node.destroy_node()
        rclpy.shutdown()    

if __name__ == '__main__':
    main()