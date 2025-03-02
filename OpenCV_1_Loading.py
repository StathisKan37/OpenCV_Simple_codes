# Importing the cv2 library as cv
import cv2 as cv

# Printing the version of OpenCV
print("OpenCV version:", cv.__version__)

# Reading the demo image and saving it in the variable 'img'
img = cv.imread('demo_image.png',cv.IMREAD_COLOR)

# Reading the demo image in grayscale and saving it
img_gray = cv.imread('demo_image.png',cv.IMREAD_GRAYSCALE)

# Alternatively:
# IMREAD_COLOR: 1
# IMREAD_GRAYSCALE: 0
# IMREAD_UNCHANGED: -1

# Displaying the images inside a window
cv.imshow('Demo image',img)  
cv.imshow('Grayscale image',img_gray)
 
# Waiting for a keystroke
cv.waitKey(0)  
 
# Destroying all the windows created
cv.destroyAllWindows() 
