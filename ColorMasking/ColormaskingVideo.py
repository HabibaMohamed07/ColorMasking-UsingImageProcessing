#did not work on colab so i did it on vscode.
import cv2
import numpy as np

lower = np.array([15, 150, 20]) 
upper = np.array([35, 255, 255]) #hna kabart range l yellow shwaya ashan y-detect range akbar mn dargat l yellow

# for the webcam
webcam_video = cv2.VideoCapture(0)

#hnloop ashan mngbsh frame wahed bs, ashan nfdal ngeeb frames lhad ma ehna n-terminate l code.
while True:
    success, video = webcam_video.read() #Read webcam 

    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(img, lower, upper) #Masking image to find the color

    cv2.imshow("mask image", mask) 
    cv2.imshow("window", video) 
    cv2.waitKey(1)