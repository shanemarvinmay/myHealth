import typer

import numpy as np
import tensorflow as tf

app = typer.Typer()
model_file_path = "model/mini_model.keras"
class_names = ["hamburger", "hot dog", "pizza"]


@app.command()
def get_nutrition_from_photo(photo_path: str):
    """get_nutrition_from_photo takes in a path to a photo of food, and prints the nutritional information.

    Args:
        photo_path (str): a path to a photo of food.
    """
    img = tf.keras.utils.load_img(photo_path)
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch
    model = tf.keras.models.load_model(model_file_path)
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    food_name = class_names[np.argmax(score)]
    confidence_score = round(100 * np.max(score), 2)
    print(f"This food is a {food_name} with a {confidence_score}% confidence.")


if __name__ == "__main__":
    app()
