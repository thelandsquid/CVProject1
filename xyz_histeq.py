from __future__ import division
import cv2
import numpy as np
import sys
import math as math

# read arguments
if(len(sys.argv) != 7) :
    print(sys.argv[0], ": takes 6 arguments. Not ", len(sys.argv)-1)
    print("Expecting arguments: w1 h1 w2 h2 ImageIn ImageOut.")
    print("Example:", sys.argv[0], " 0.2 0.1 0.8 0.5 fruits.jpg out.png")
    sys.exit()

w1 = float(sys.argv[1])
h1 = float(sys.argv[2])
w2 = float(sys.argv[3])
h2 = float(sys.argv[4])
name_input = sys.argv[5]
name_output = sys.argv[6]

# check the correctness of the input parameters
if(w1<0 or h1<0 or w2<=w1 or h2<=h1 or w2>1 or h2>1) :
    print(" arguments must satisfy 0 <= w1 < w2 <= 1, 0 <= h1 < h2 <= 1")
    sys.exit()

# read image
inputImage = cv2.imread(name_input, cv2.IMREAD_COLOR)
if(inputImage is None) :
    print(sys.argv[0], ": Failed to read image from: ", name_input)
    sys.exit()

# check for color image and change w1, w2, h1, h2 to pixel locations
rows, cols, bands = inputImage.shape
if(bands != 3) :
    print("Input image is not a standard color image:", inputImage)
    sys.exit()

W1 = int(round(w1*(cols-1)))
H1 = int(round(h1*(rows-1)))
W2 = int(round(w2*(cols-1)))
H2 = int(round(h2*(rows-1)))

inputImage = cv2.cvtColor(inputImage , cv2.COLOR_BGR2XYZ)
output_gray_image = cv2.equalizeHist(inputImage[H1:H2,W1:W2,1])

tmp1 = np.copy(inputImage)
tmp1[H1:H2,W1:W2,1] = output_gray_image

cv2.imshow("xyz_histeq", cv2.cvtColor(tmp1,cv2.COLOR_XYZ2BGR))

# saving the output - save the gray window image
cv2.imwrite(name_output, tmp1)

# wait for key to exit
cv2.waitKey(0)
cv2.destroyAllWindows()