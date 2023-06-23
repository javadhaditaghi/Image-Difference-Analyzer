from flask import Flask, render_template, request, send_file, after_this_request
import cv2 as cv
import numpy as np
import os

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    # Check if the request contains the files 'picture_1' and 'picture_2'
    if 'picture_1' in request.files and 'picture_2' in request.files:
        picture_1 = request.files['picture_1']
        picture_2 = request.files['picture_2']

        # Save 'picture_1' with its original filename in the 'static' folder
        picture_1.save('static/' + picture_1.filename)

        # Save 'picture_2' with its original filename in the 'static' folder
        picture_2.save('static/' + picture_2.filename)

        # Process the images
        path_1 = 'static/' + picture_1.filename
        path_2 = 'static/' + picture_2.filename

        image = cv.imread(path_1, 0)
        image_1 = cv.imread(path_2, 0)
        image_1 = cv.resize(image_1, (image.shape[1], image.shape[0]))
        image_2 = np.zeros(image.shape, np.uint8)

        for i in range(image.shape[0]):
            for j in range(image_1.shape[1]):
                if image[i, j] > image_1[i, j]:
                    image_2[i, j] = image[i, j] - image_1[i, j]
                else:
                    image_2[i, j] = 0

        image_2 *= 2
        # Resize the resulting image to a fixed size of 500x500 pixels
        image_2 = cv.resize(image_2, (650, 650))

        # Save the resulting image
        result_path = os.path.join('static', 'result.jpg')
        cv.imwrite(result_path, image_2)

        @after_this_request
        def remove_uploaded_files(response):
            # Remove the uploaded pictures
            os.remove('static/' + picture_1.filename)
            os.remove('static/' + picture_2.filename)
            return response

        return render_template('result.html', result_path=result_path)


    else:
        return 'One or both pictures are missing in the request.'


@app.route('/static/result.jpg')
def get_result():
    return send_file('static/result.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    app.run()
