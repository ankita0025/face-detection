import cv2

 
#load some pre-trained data on face frontals from opencv(harcascade algorithm)
#here we are calling the classifying function which is used to detect things
trained_face_data= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image to detect image
#img = cv2.imread("WIN_20190421_04_47_17_Pro.jpg") 

#to capture video from webcam
webcam = cv2.VideoCapture(0)

#iterate throught the frames in video
while True:

    #read the current frame
    successful_frame_read, frame = webcam.read()
    
    #converting the image into greyscale
    greyscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces it returns the coordinates of the rectangle 
    face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)


    for(x,y,w,h) in face_coordinates:
        cv2.rectangle(frame , (x,y),(x+w,y+h),(0,255,0),2)

    #for showing the image
    cv2.imshow("ankit's face detector",frame)

    #fir pausing the display of image until a key is pressed
    cv2.waitKey(1)

    print("code completed")

"""
#detect faces it returns the coordinates of the rectangle 
face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

for(x,y,w,h) in face_coordinates:
    cv2.rectangle(img , (x,y),(x+w,y+h),(0,255,0),2)

print(face_coordinates)

#for showing the image
cv2.imshow("ankit's face detector",img)

#fir pausing the display of image until a key is pressed
cv2.waitKey()

print("code completed")
"""