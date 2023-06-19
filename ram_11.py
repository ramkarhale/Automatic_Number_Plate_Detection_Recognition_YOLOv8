import glob
import cv2


path="C:\\Users\\DELL\\Techathon\\Automatic_Number_Plate_Detection_Recognition_YOLOv8\\Scanned_image1\\*.jpg"    #Replace with your folder 
images = [cv2.imread(images) for images in glob.glob(path)]

print(len(images))     #number of images in folder
for i in range(len(images)):
    cv2.imshow("images",images[i])
    cv2.waitKey(0)