import numpy as np
import tensorflow as tf
from . import path
import os

batch_size = 32
img_height = 180
img_width = 180

model = os.path.join(path.STATIC_DIR, 'model', 'myanmar_clothes_model_v2_0.h5')
class_names = ['amarapura_design', 'chate_design',
               'innlay_design', 'sanmyan_design']

# load model
new_model = tf.keras.models.load_model(model)


def detection(image):

    img = tf.keras.utils.load_img(
        image, target_size=(img_height, img_width)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    # use new_model
    predictions = new_model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print("Detecting .... ")
    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )

    return class_names[np.argmax(score)], (100 * np.max(score))


#image = 'test_img/amarapura1.jpg'
#detection(image, model, class_names)
