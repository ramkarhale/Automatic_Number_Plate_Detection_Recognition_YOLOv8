import cv2

minArea = 500
_x = 0
nPlate_cascade = cv2.CascadeClassifier('raw.githubusercontent.com_opencv_opencv_master_data_haarcascades_haarcascade_russian_plate_number.xml')


vidcap = cv2.VideoCapture('demo.mp4')
def getFrame(sec):
    count_1 = 0
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()

    if hasFrames:
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        numberPlate = nPlate_cascade.detectMultiScale(gray,1.1,4)

        for(x,y,w,h) in numberPlate:
            area = w*h
            if area>minArea:
                cv2.rectangle(image ,(x,y),(x+w,y+h),(255,0,0),3)
                cv2.putText(image,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),1)
                imgRoi= image[y:y+h,x:x+w]
                #cv2.imshow("ROI",imgRoi)
                cv2.imwrite('C:/Users/DELL/Techathon/Automatic_Number_Plate_Detection_Recognition_YOLOv8/Scanned_images/ram_'+str(count_1)+".jpg",imgRoi)
                count_1 = count_1+1
                cv2.waitKey(5)
         #cv2.imwrite('C:/Users/DELL/Techathon/Automatic_Number_Plate_Detection_Recognition_YOLOv8/Scanned_image1/ram_'+str(count)+".jpg",image)     # save frame as JPG file
    return hasFrames

sec = 0
frameRate = 1 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)    
