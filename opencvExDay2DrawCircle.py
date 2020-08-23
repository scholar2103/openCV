import cv2 as cv
import numpy as np

# mouse callback function
def onClick(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y), 3, (255,255,255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv.line(img,points[-1],points[-2],(255,255,0),2, cv.LINE_AA)
        

img = cv.imread("aloeL.jpg",1)
cv.imshow("image",img)

# create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
points = []
# cv.namedWindow("image")
cv.setMouseCallback("image", onClick)

while(1):
    cv.imshow("image",img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()

# mouse callback function
# def draw_circle(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img,(x,y),100,(255,0,0),-1)

# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)

