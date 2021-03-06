# USAGE
# python stitch.py --first images/bryce_left_01.png --second images/bryce_right_01.png 

# import the necessary packages
from pyimagesearch.panorama import Stitcher
import argparse
import imutils
import cv2



imageA = cv2.imread('images/grand_canyon_left_02.png')
imageB = cv2.imread('images/grand_canyon_right_02.png')

imageA = imutils.resize(imageA, width=1000)
imageB = imutils.resize(imageB, width=1000)

# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.waitKey(0)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)