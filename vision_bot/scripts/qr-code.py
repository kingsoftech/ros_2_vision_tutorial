import cv2
#fetching the image directory
img = cv2.imread('/home/abdullah/ros2_workspace/src/ros_2_vision_tutorial/vision_bot/meshes/left.png')

#creating an opencv object decoder
decoder = cv2.QRcodeDetector()

#getting the object and data
data, points, _ = decoder.detectAndDecode(img)

#printing out the result
print("results = ", data)
#viewing the image
cv2.imshow("Detected QR code is, ", img)
#initializing press any key to exit
cv2.waitKey()

#destroys all opened windows when exited
cv2.destroyAllWindows()
