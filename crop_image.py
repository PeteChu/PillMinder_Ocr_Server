import cv2
import os

from numba import jit

@jit
def crop(image_path):

    image = cv2.imread(image_path)

    original_image = image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    rect, threshold = cv2.threshold(
        blur, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    im2, contours, hierarchy = cv2.findContours(
        threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:

        # draw contours
        cv2.drawContours(original_image, contours, -1, 255, 3)

        # find largest contour
        c = max(contours, key=cv2.contourArea)

        x,y,w,h = cv2.boundingRect(c)

    return original_image[y: y+h, x:x+w]