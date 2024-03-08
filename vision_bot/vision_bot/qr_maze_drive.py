import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2

class lidar_camera_sub(Node):

    def __init__(self):
        super().__init__('qr_maze_solving_node')
        self.subscription = self.create_subscription(Image,'/vision_bot_camera/image_raw',self.camera_callback,10)
        self.bridge = CvBridge()
        self.frame=0
        

    def camera_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg.data,'bgr8')
        self.get_logger().info('I heard: "%d"' % msg.data)
        cv2.imshow('Frame', self.frame)
        cv2.waitKey

def main(args=None):
    rclpy.init(args=args)

    simple_sensor_sub = lidar_camera_sub()

    rclpy.spin(simple_sensor_sub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    simple_sensor_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()