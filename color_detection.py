import cv2
import numpy

#we will be  using trackbars to find out min and max HSV values

#creating new  window for hsv trackbars
windowName="HSV"
cv2.namedWindow(windowName)

image=cv2.imread("images/rose.jpeg")
hsvImage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

def  onchangefunc(dummyArgument):
    #initially let onchange be empty
    # get all trackbar values
    hue_min=cv2.getTrackbarPos(trackbarname="Hue min",winname=windowName)
    hue_max=cv2.getTrackbarPos(trackbarname="Hue max",winname=windowName)
    sat_min=cv2.getTrackbarPos(trackbarname="Saturation min",winname=windowName)
    sat_max=cv2.getTrackbarPos(trackbarname="Saturation max",winname=windowName)
    val_min=cv2.getTrackbarPos(trackbarname="Value min",winname=windowName)
    val_max=cv2.getTrackbarPos(trackbarname="Value max",winname=windowName)
    print((hue_min,sat_min,val_min),(hue_max,sat_max,val_max))

    # let's create mask
    minHSV=numpy.array([hue_min,sat_min,val_min])
    maxHSV=numpy.array([hue_max,sat_max,val_max])
    mask=cv2.inRange(hsvImage,minHSV,maxHSV)   # adjust values of trackbars to get your required color in white and remaining in black
    cv2.imshow("mask",mask)
    # now we got HSV range for our rose color
    #minHSV=(141,175,0)
    #maxHSV=(179,255,255)

# we have to add 6 trackbars to window
# cv2.createTrackbar(trackbarName=,windowName,value,count,onChange=onchangefunc)
# value - initial value when trackbar created
# count - max value for trackbar
# onChange - function that will execute when trackbar value is changed


cv2.createTrackbar("Hue min", windowName,0,179,onchangefunc) #windowName must be the name of window we created
cv2.createTrackbar("Hue max",windowName,0,179,onchangefunc)
cv2.createTrackbar("Saturation min",windowName,0,255,onchangefunc)
cv2.createTrackbar("Saturation max",windowName,0,255,onchangefunc)
cv2.createTrackbar("Value min",windowName,0,255,onchangefunc)
cv2.createTrackbar("Value max",windowName,0,255,onchangefunc)

cv2.imshow("rose",image)
# now we are going to create HSV image using cvtColor

cv2.imshow("HSV rose",hsvImage)

#this is our HSV image
# now we are ready to chnage onchnagefunc method

minHSV=(141,175,0)
maxHSV=(179,255,255)
# for final ouput
mask = cv2.inRange(hsvImage, minHSV,maxHSV)
finalImage=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("final image",finalImage)

cv2.waitKey(0)
