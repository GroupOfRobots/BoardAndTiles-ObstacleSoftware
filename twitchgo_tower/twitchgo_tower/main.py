import rclpy
from twitchgo_tower.tower_node import TowerNode
    
def main(args=None):
    rclpy.init(args=args)
    tower_node = TowerNode()
    rclpy.spin(tower_node)

    tower_node.destroy_node()
    rclpy.shutdown()

    
if __name__ == '__main__':
    main()