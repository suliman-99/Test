import tensorflow as tf
import keras.utils as image
import numpy as np


def mri_clasification():
    MRIclf = tf.keras.models.load_model('Assets/MRI.keras')
    MRIclf.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Define image dimensions
    img_height, img_width = 176, 208

    # Load a new image for prediction
    # new_image_path = 'Assets/VMD.jpg'
    # new_image_path = 'Assets/ND.jpg'
    # new_image_path = 'Assets/MoD.jpg'
    new_image_path = 'Assets/MD.jpg'

    # Load and preprocess the image
    new_img = image.load_img(new_image_path, target_size=(img_height, img_width))
    new_img_array = image.img_to_array(new_img)
    new_img_array = np.expand_dims(new_img_array, axis=0)

    # Make predictions
    predictions = MRIclf.predict(new_img_array)

    # Decode predictions (convert numerical labels to class names)
    class_names = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']
    predicted_class_index = np.argmax(predictions[0])
    predicted_class_value = predictions[0][predicted_class_index]
    predicted_class_name = class_names[predicted_class_index]

    print("Predicted Class:", predicted_class_name)
    print("Predicted Probabilities:", predicted_class_value)

    return predicted_class_value
