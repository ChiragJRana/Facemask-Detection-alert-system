import numpy as np 
import cv2
import os
from django.conf import settings
face_cascade = cv2.CascadeClassifier(os.path.join(settings.BASE_DIR,'cascades/data/haarcascade_frontalface_alt2.xml'))
profile_face_cascade = cv2.CascadeClassifier('cascades\data\haarcascade_profileface.xml')

# checking the working of the camera =================================================
# print(cv2.__version__)

# cap = cv2.VideoCapture(0) # there is method to select multiplee cameras
# while True : # continuous  read of a frame 
#     ret, frame = cap.read()
#     # convert image to gray 
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame',gray)
#     cv2.imshow('frame1',frame)
   
#     cv2.waitKey(1)
#     if cv2.waitKey(2) & 0xFF == ord('q'):

#         break
# ====================================================================================


# # Checking the detection working or not==================================================

# # print(help(cv2.face))
# cap = cv2.VideoCapture(0)

# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
	
# 	# convert the grames to gray
#     gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # this method will detect the face and return an object with its dimentions
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) # for the front face
#     # profile = profile_face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) # for the side face 
#     # profile_flip = profile_face_cascade.detectMultiScale(cv2.flip(gray,1), scaleFactor=1.5, minNeighbors=5) # for the flipped side face


# # # loop for box around the profile
#     # for (x, y, w, h) in profile:
#     #     print(x,y,w,h)
#     #     roi_gray = gray[y:y+h, x:x+w]
#     #     roi_color = frame[y:y+h, x:x+h]

#     #     img_item = "images/my_image.png"
#     #     cv2.imwrite(img_item, roi_gray)

#     #     # Create a box around the face
#     #     color = (255,0,0)
#     #     stroke = 2

#     #     cv2.rectangle(frame, (x,y), (x+w, y+h), color, stroke)

# # # loop for box around the flipped-profile

#     # for (x, y, w, h) in profile_flip:
#     #     print(x,y,w,h)
#     #     roi_gray = gray[y:y+h, x:x+w]
#     #     roi_color = frame[y:y+h, x:x+h]

#     #     img_item = "images/my_image.png"
#     #     cv2.imwrite(img_item, roi_gray)

#     #     # Create a box around the face
#     #     color = (255,0,0)
#     #     stroke = 2

#     #     cv2.rectangle(frame, (x,y), (x+w, y+h), color, stroke)
        

#     for (x, y, w, h) in faces:
        
#         # Create a box around the face
#         color = (255,0,0)
#         stroke = 2

#         cv2.rectangle(frame, (x,y), (x+w, y+h), color, stroke)

#     # Display the resulting frame
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
# # ========================================================================


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    
    def get_frame(self):
        ret, frame = self.video.read()
	
	    # convert the grames to gray
        gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # this method will detect the face and return an object with its dimentions
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        profile = profile_face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) # for the side face 
        profile_flip = profile_face_cascade.detectMultiScale(cv2.flip(gray,1), scaleFactor=1.5, minNeighbors=5) # for the flipped side face
        print('Streaming_Video')
        # # loop for box around the profile
        for (x, y, w, h) in profile:
            
            # Create a box around the face
            color = (255,0,0)
            stroke = 2

            cv2.rectangle(frame, (x,y), (x+w, y+h), color, stroke)

        # loop for box around the flipped-profile

        for (x, y, w, h) in profile_flip:
            
            # Create a box around the face
            color = (255,0,0)
            stroke = 2

            cv2.rectangle(frame, (x,y), (x+w, y+h), color, stroke)

        #  create the frame for the face the detected only the frontal part.
        for (x, y, w, h) in faces:

            # Create a box around the face
            color = (255,0,0)
            stroke = 2

            cv2.rectangle(frame, (x,y), (x+w, y+h), color, stroke)
        
        # flip the image as opencv doesnt how mirror image if not included still not a problem
        frame_flip = cv2.flip(frame,1)
        ret, jpeg = cv2.imencode('.jpg', frame_flip)
        return jpeg.tobytes()

