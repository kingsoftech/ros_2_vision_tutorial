from pyzbar.pyzbar import decode
import cv2

# Fetching the image directory
img = cv2.imread('/home/abdullah/ros2_workspace/src/ros_2_vision_tutorial/vision_bot/meshes/left.png')

# Converting the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Getting the decoded objects and data
decoded_objs = decode(gray_img)

# Looping through the decoded objects
for obj in decoded_objs:
    data = obj.data.decode('utf-8')
    print("Result:", data)

# Displaying the image
cv2.imshow("Detected QR code", img)

# Initializing press any key to exit
cv2.waitKey(0)

# Destroys all opened windows when exited
cv2.destroyAllWindows()


#destroys all opened windows when exited
cv2.destroyAllWindows()
