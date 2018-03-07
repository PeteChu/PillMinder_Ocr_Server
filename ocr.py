from PIL import Image
import cv2
import pytesseract
import os
import re

from numba import jit


def cvtToBw(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.medianBlur(gray, 3)
    rect, bw_image = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    filename = './images/ocr/{}.jpg'.format(os.getpid())
    cv2.imwrite(filename, bw_image)
    return filename


def imageToText(image):

    tessdata_dir_config = '--tessdata-dir "./tessdata"'

    bw_image_path = cvtToBw(image)

    text = pytesseract.image_to_string(Image.open(
        bw_image_path), lang='tha+eng', config=tessdata_dir_config)

    os.remove(bw_image_path)

    pattern = re.compile('[^a-zA-Z ]')
    text = pattern.sub('', text)

    return [i for i in text.split() if len(i) > 3]
