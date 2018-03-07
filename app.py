import cv2
from crop_image import crop
from ocr import imageToText
from difflib import get_close_matches

# def findMedicineName(medicine_list, text):

#     for i in range(len(medicine_list)):
#         word = medicine_list[i]
#         length = len(word)
#         for j in range(len(text)):
#             if j+length < len(text):
#                 tmp = text[j: j+length]
#                 close_match = get_close_matches(tmp, medicine_list, cutoff=0.8)
#                 if close_match:
#                     return close_match[0]
#     return -1

def findMedicineName(medicine_list, text_list):

    for i in text_list:
        close_match = get_close_matches(i, medicine_list)
        if close_match:
            return close_match[0]
    return -1

if __name__ == '__main__':

    medicine_list = ["AMLODIPINE"]

    image_path = './images/image1.jpg'
    image = cv2.imread(image_path)

    cropped_image = crop(image)

    text_list = imageToText(cropped_image)

    medicine_name = findMedicineName(medicine_list, text_list)

    print(medicine_name)
