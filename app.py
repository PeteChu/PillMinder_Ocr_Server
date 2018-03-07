import cv2
from crop_image import crop
from ocr import image_to_text

if __name__ == '__main__':

    image_path = './images/image1.jpg'
    image = cv2.imread(image_path)

    cropped_image = crop(image)

    text = image_to_text(cropped_image)

    print(text)

