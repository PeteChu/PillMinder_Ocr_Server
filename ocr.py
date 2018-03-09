from PIL import Image
import cv2
import pytesseract
import os
import re

import time

from numba import jit


def cvtToBw(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.medianBlur(gray, 3)
    rect, bw_image = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    filename = './images/ocr/{}.jpg'.format(os.getpid())
    cv2.imwrite(filename, bw_image)
    return filename


def show_state(msg):
    print(msg)


def imageToText(image):

    tessdata_dir_config = '--tessdata-dir "./tessdata"'

    start = time.time()

    show_state("Img2text: cvt2bw {}".format(time.time()))

    bw_image_path = cvtToBw(image)

    show_state("Img2text: start ocr {}".format(time.time()))
    text = pytesseract.image_to_string(Image.open(
        bw_image_path), lang='tha', config=tessdata_dir_config)

    show_state("Img2text: ocr done {}".format(time.time()))
    # os.remove(bw_image_path)

    print(text)

    show_state("Img2text: start regex {}".format(time.time()))
    pattern = re.compile('[^a-zA-Z ]')
    text = pattern.sub('', text)

    show_state("Img2text:  regex done {}".format(time.time()))

    stop = time.time()

    print(stop - start)
    return [i for i in text.split() if len(i) > 3]
