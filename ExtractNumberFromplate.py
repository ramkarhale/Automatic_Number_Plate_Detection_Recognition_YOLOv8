#Addition of two number 

import numpy as np
import cv2
import os
import glob
import easyocr
from os import listdir

minArea = 500
count = 0
_x = 0
nPlate_cascade = cv2.CascadeClassifier('raw.githubusercontent.com_opencv_opencv_master_data_haarcascades_haarcascade_russian_plate_number.xml') #russian number plates video


reader = easyocr.Reader(['en'])
while _x < 2:
    path="C:\\Users\\DELL\\Techathon\\Automatic_Number_Plate_Detection_Recognition_YOLOv8\\Scanned_image1\\*.jpg"    #images extracted from video and store here (and taken one by one for process)
    images = [cv2.imread(images) for images in glob.glob(path)]

    for i in range(len(images)): # iterrate through images
        #img = cv2.imread('Screenshot (1).png')
        gray = cv2.cvtColor(images[i],cv2.COLOR_BGR2GRAY)
        numberPlate = nPlate_cascade.detectMultiScale(gray,1.1,4) #Detect number plate from image

        for(x,y,w,h) in numberPlate:
            area = w*h
            if area > minArea:
                cv2.rectangle(images[i] ,(x,y),(x+w,y+h),(255,0,0),3)
                cv2.putText(images[i],"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),1)
                imgRoi = images[i][y:y+h,x:x+w]  # Region of interest (Only number plate)
                #cv2.imshow("ROI",imgRoi)
                roi_gray_1 = cv2.cvtColor(imgRoi,cv2.COLOR_BGR2GRAY)
                #cv2.imshow("ROI",roi_gray_1)
                #_,roi_threshhold = cv2.threshold(roi_gray_1,64,255,cv2.THRESH_BINARY)
                #cv2.imshow("ROI",roi_threshhold)
                output = reader.readtext(roi_gray_1)
                for out in output:
                    text_bbox,text,text_score = out
                    print(text,text_score)   # Print text on number plate and accuracy of prediction

                cv2.imwrite('C:/Users/DELL/Techathon/Automatic_Number_Plate_Detection_Recognition_YOLOv8/Scanned_images/ram_'+str(count)+".jpg",imgRoi) #Stored plate image intp the folder
                count = count+1
                cv2.waitKey(0)
        _x = _x+1
