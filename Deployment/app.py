import pickle
import numpy as np
import tensorflow as tf
from keras.models import load_model
from flask import Flask, request, render_template


app = Flask(__name__)
text_model = pickle.load(open('text-model.pkl', 'rb'))
image_model = load_model('image-model.h5')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

    file = request.files['product_image']
    img_new = 'datasets/images/'+file.filename
    img_height = 80
    img_width = 60
    class_names = ['bag', 'prohibited', 'slipper', 'sunglass', 'tail', 'watch']

    img = tf.keras.utils.load_img(img_new, target_size=(img_height, img_width)) # Load image and resize it with (60*80)
    img_array = tf.keras.utils.img_to_array(img) # Convert to array
    img_array_res = tf.expand_dims(img_array, 0) # Create a batch


    title = request.form.get('product_title')
    text_prediction = text_model.predict([format(title)])

    imagePre = image_model.predict(img_array_res)
    resu = tf.nn.softmax(imagePre[0])

    return render_template('index.html', prediction_text=' {}'.format(text_prediction[0]), prediction_image = class_names[np.argmax(resu)] ) #.format(text_prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)