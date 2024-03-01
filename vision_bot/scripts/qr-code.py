import cv2

img = cv2.imread('/home/abdullah/ros2_workspace/src/ros_2_vision_tutorial/vision_bot/meshes/left.png')
decoder = cv2.QRcodeDetector()
data, points, _ = decoder.detectAndDecode(img)

print("results = ", data)
cv2.imshow("Detected QR code is, ", img)
cv2.waitKey()
cv2.destroyAllWindows()
