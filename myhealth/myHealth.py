from prettytable import PrettyTable
from tinydb import TinyDB, Query

import typer
import numpy as np
import tensorflow as tf
from typing import List

app = typer.Typer()
model_file_path = "model/mini_model.keras"
class_names = ["hamburger", "hot dog", "pizza"]


def get_food_name_from_user() -> str:
    food_name = input("Enter food name (type quit to quit):").lower()
    if food_name == "quit":
        exit()
    return food_name


def get_nutritional_data_for_food(food_name: str) -> List:
    db = TinyDB("data/db.json")
    Food = Query()
    results = db.search(Food.name == food_name)
    if len(results) > 0:
        return results
    # Check secondary db.
    db = TinyDB("data/secondary_db.json")
    for food in db:
        for food_id in food:
            if food_name in food[food_id]["name"]:
                results.append(food[food_id])
    if len(results) > 0:
        return results
    # No food found. Exiting program
    print(f"No nutritional data for '{food_name.title()}'")
    exit()


def print_nutritional_data(nutritional_data: dict):
    # Print food name
    food_name = nutritional_data.get("name", "UNKNOWN FOOD NAME").title()
    print(f"\n{food_name}")
    # Print serving size disclosure
    print("The following metrics are based on a 100g serving size.")
    # Print Nutrients
    table = PrettyTable()
    table.field_names = ["Nutrient", "Amount"]
    for attr in nutritional_data:
        if attr == "name":
            continue
        nutrient_name = attr.title()
        nutrient_value = round(nutritional_data[attr], 4)
        table.add_row([nutrient_name, nutrient_value])
    print(table)


@app.command()
def get_nutrition_from_photo(photo_path: str):
    """get_nutrition_from_photo takes in a path to a photo of food, and prints the nutritional information.

    Args:
        photo_path (str): a path to a photo of food.
    """
    # Running the model on the image that was provided.
    img = tf.keras.utils.load_img(photo_path)
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch
    model = tf.keras.models.load_model(model_file_path)
    predictions = model.predict(img_array)
    scores = tf.nn.softmax(predictions[0])
    highest_score_highest_idx = np.argmax(scores)

    if scores[highest_score_highest_idx] < 0.8:
        print("Mmmmm... I don't recognize that food by the picture.")
        food_name = get_food_name_from_user()
    else:
        food_name = class_names[highest_score_highest_idx]
        confidence_score = round(100 * np.max(scores), 2)
        print(f"This food is a {food_name} with a {confidence_score}% confidence.")
    nutritional_data_results = get_nutritional_data_for_food(food_name)
    for nutritional_data in nutritional_data_results:
        print_nutritional_data(nutritional_data)


if __name__ == "__main__":
    app()
