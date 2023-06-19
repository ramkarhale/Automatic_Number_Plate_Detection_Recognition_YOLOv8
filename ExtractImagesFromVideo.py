
import cv2
vidcap = cv2.VideoCapture('demo.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
         cv2.imwrite('C:/Users/DELL/Techathon/Automatic_Number_Plate_Detection_Recognition_YOLOv8/Scanned_image1/ram_'+str(count)+".jpg",image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 1.54545455 #//it will capture image in each 0.5 second
count = 1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)    

