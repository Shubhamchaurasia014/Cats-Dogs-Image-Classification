import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("cats_dogs_model.h5")

# Streamlit App Layout

st.title("🐱🐶 Cats vs Dogs Classifier")
st.write("Upload an image and the model will predict whether it's a cat or a dog.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    img = image.resize((128, 128))   # match training size
    img_array = tf.keras.utils.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # normalize

    # Prediction
    prediction = model.predict(img_array)

    # Assuming binary classification: 0 = cat, 1 = dog
    if prediction[0][0] > 0.5:
        st.success("🐶 It's a Dog!")
    else:
        st.success("🐱 It's a Cat!")