import typer

import numpy as np
import tensorflow as tf

app = typer.Typer()
model_file_path = 'model/mini_model.keras'
class_names = ['hamburger', 'hot dog', 'pizza']

@app.command()
def get_nutrition_from_photo(photo_path: str):
    """Upload photo based on file path.
    """    
    img = tf.keras.utils.load_img(photo_path)
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    model = tf.keras.models.load_model(model_file_path)
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    print( "This image most likely belongs to {} with a {:.2f} percent confidence." .format(class_names[np.argmax(score)], 100 * np.max(score)) )

if __name__ == "__main__":
    app()
