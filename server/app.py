from flask import Flask
from flask_restful import Resource, Api
from upload_img import uploadImg

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
api.add_resource(uploadImg, '/uploadimg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)