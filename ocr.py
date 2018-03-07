from PIL import Image
import cv2
import pytesseract
import os


def cvt_to_bw(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    rect, bw_image = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    blur = cv2.GaussianBlur(bw_image, (0, 0), 3)

    filename = './images/ocr/{}.jpg'.format(os.getpid())
    cv2.imwrite(filename, blur)
    return filename


def image_to_text(image_path):

    tessdata_dir_config = '--tessdata-dir "./langdata"'

    bw_image_path = cvt_to_bw(image_path)

    text = pytesseract.image_to_string(Image.open(
        bw_image_path), lang='tha+eng', config=tessdata_dir_config)
    os.remove(bw_image_path)

    return text
