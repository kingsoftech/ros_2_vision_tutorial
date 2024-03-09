import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class camera_sub(Node):

    def __init__(self):
        super().__init__('line_node')
        self.camera_sub = self.create_subscription(Image,'/vision_bot_camera/image_raw',self.camera_cb,10)
       

        self.bridge=CvBridge()
        self.frame=0


    def camera_cb(self, data):
        self.frame = self.bridge.imgmsg_to_cv2(data,"bgr8")
        cv2.imshow('Frame',self.frame)
        cv2.waitKey(1)

 

    def qr_detector(self):
        decoder = cv2.QRCodeDetector()
        data, points, _ = decoder.detectAndDecode(self.frame)
        print(data)

def main(args=None):
    rclpy.init(args=args)

    sensor_sub = camera_sub()

    rclpy.spin(sensor_sub)
    sensor_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()