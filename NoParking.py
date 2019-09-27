import cv2
import time

from gui import gui
from main import preprocess,extract_contours,cleanAndRead
windowname="Live Video"
gui()
cap=cv2.VideoCapture(0)
t=3
if cap.isOpened():
       ret,frame=cap.read()
else:
       ret=False
while False:
      
      ret,img=cap.read()
      #time.sleep(t)
      cv2.imshow(windowname,img)
      print ("DETECTING PLATE . . .")
#img = cv2.imread("testData/Final.JPG")
      threshold_img = preprocess(img)
      contours= extract_contours(threshold_img)
	#if len(contours)!=0:
		#print len(contours) #Test
		# cv2.drawContours(img, contours, -1, (0,255,0), 1)
		# cv2.imshow("Contours",img)
		# cv2.waitKey(0)


      cleanAndRead(img,contours)
      if cv2.waitKey(1)==27:
         break;
cv2.destroyAllWindows()
cap.release()
        
