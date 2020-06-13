import cv2

cap = cv2.VideoCapture(0);      # for live system camera
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
#cap = cv2.VideoCapture('filename.mp4');     #for a video store in system
print(cap.isOpened())
while (True):
    ret, frame = cap.read()     #ret stores 'true' or 'false' and frame is the variable to store data which we are reading
    if ret == True:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))      #for frame width and height
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)  # for making a copy

        #grey = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)    #for converting into grey color
        #cv2.imshow('frame', grey)


        cv2.imshow('frame', frame)  #to show in normal color
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()