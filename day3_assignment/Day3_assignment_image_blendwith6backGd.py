
import cv2

import numpy as np
import sys
cap = cv2.VideoCapture(0)
image=cv2.imread('C:/Face_recognition/project_opencv/Tom&jerry.jpg')
image2=cv2.imread('C:/Face_recognition/project_opencv/background2.jpg')
image3=cv2.imread('C:/Face_recognition/project_opencv/background3.jpg')
image4=cv2.imread('C:/Face_recognition/project_opencv/backgroun4.jpg')
image5=cv2.imread('C:/Face_recognition/project_opencv/background5.jpg')
image6=cv2.imread('C:/Face_recognition/project_opencv/Background6.jpg')
option = int(input("Enter the number: "))
#cap=cv2.VideoCapture('C:/Users/chira/Downloads/videogoku.mp4')
while True:
    flag, frame = cap.read()
    if not flag:
        print("Couldnot access")
        break
    elif flag:
        if option==1:
             image = cv2.resize(image, (frame.shape[1],frame.shape[0]))
             bkgrnd_frame=cv2.addWeighted(frame, 0.8,image, 0.2, gamma= 0.1)
             cv2.imshow('Frame',bkgrnd_frame)
             if cv2.waitKey(10) & 0xFF == ord('s'):

                    sys.exit(),
        elif option==2:
             image2 = cv2.resize(image2, (frame.shape[1],frame.shape[0]))
             bkgrnd_frame2=cv2.addWeighted(frame, 0.2,image2, 0.8, gamma= 0.2)
             cv2.imshow('Frame',bkgrnd_frame2)
             if cv2.waitKey(10) & 0xff == ord('a'):
                  sys.exit()
        elif option==3:        
             image3 = cv2.resize(image3, (frame.shape[1],frame.shape[0]))
             bkgrnd_frame3=cv2.addWeighted(frame, 0.2,image3, 0.8, gamma= 0.2)
             cv2.imshow('Frame',bkgrnd_frame3)
             if cv2.waitKey(10) & 0xff == ord('b'):
                  sys.exit()
        elif option==4:        
             image4 = cv2.resize(image4, (frame.shape[1],frame.shape[0]))
             bkgrnd_frame4=cv2.addWeighted(frame, 0.2,image4, 0.8, gamma= 0.2)
             cv2.imshow('Frame',bkgrnd_frame4)
             if cv2.waitKey(10) & 0xff == ord('c'):
                  sys.exit()
        elif option==5:        
             image5 = cv2.resize(image5, (frame.shape[1],frame.shape[0]))
             bkgrnd_frame5=cv2.addWeighted(frame, 0.2,image5, 0.8, gamma= 0.2)
             cv2.imshow('Frame',bkgrnd_frame5)
             if cv2.waitKey(10) & 0xff == ord('d'):
                  sys.exit()
        elif option==6:        
             image6 = cv2.resize(image6, (frame.shape[1],frame.shape[0]))
             bkgrnd_frame6=cv2.addWeighted(frame, 0.2,image6, 0.8, gamma= 0.2)
             cv2.imshow('Frame',bkgrnd_frame6)
             if cv2.waitKey(10) & 0xff == ord('e'):
                  sys.exit()
        else:
            print("try again")
               
cap.release()
cv2.destroyAllWindows()