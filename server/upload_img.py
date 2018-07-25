from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import sys
import os
import uuid
import json

sys.path.append('./../ocr')

from ocr import imageToText
from find_medicine_name import findMedicineName

IMAGES_DIR = './../images'

class uploadImg(Resource):
    def post(self):
        image = request.files['image']
        extension = os.path.splitext(image.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        file_path = os.path.join(IMAGES_DIR, f_name)
        image.save(file_path)
        text = imageToText(file_path)
        close_matches = findMedicineName(text)
        print(close_matches)
        return {'status': 200, 'file_path': file_path, 'text': text, 'closeMatches': close_matches}
