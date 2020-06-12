import cv2

img = cv2.imread('thor.jpg', 1)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27 :     #Esc key
    cv2.destroyAllWindows()
elif k == ord('s'):     #s is for saving it again
    cv2.imwrite('thor.png', img)
    cv2.destroyAllWindows()