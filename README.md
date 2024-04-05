# Getting started working on myHealth!

## Using Poetry
* [For more information on Poetry](https://python-poetry.org/)

### Install dependencies
```
poetry install
```

### Add dependencies
```
poetry add [package-name]
```

### Activate Poetry Virtual Environment
```
poetry shell
```

### Exit Poetry's Virtual Environment
```
exit
```

### Run cmds
```
poetry run [cmd]
```
* Like black or pytest.

# To build this project
```
poetry build
```

# To publish this project
```
poetry publish
```

---

# Typer
*Typer* is the tool we will use to create the CLI (command line interface).

* [Getting started with Typer](https://typer.tiangolo.com/)
    * [A more in depth introduction](https://typer.tiangolo.com/tutorial/)
* [Hints and docstrings](https://typer.tiangolo.com/tutorial/arguments/help/)
* [Testing Typer apps](https://typer.tiangolo.com/tutorial/testing/)
* [Packaging Typer to publish](https://typer.tiangolo.com/tutorial/package/)

---

# Model

# Mini Model
* used for development and demo purposes.
* Followed [this tutorial](https://www.tensorflow.org/tutorials/images/classification) (among a few others)
    * Used [this tutorial](https://www.tensorflow.org/guide/keras/serialization_and_saving) in particular to save and load the model.
## Performance
![Second iteration resulting in ~75% accuracy](model/model_perf_mini_2.png)

---

# Data Sources
# [AI Crowd Food Recognition 2022](https://www.aicrowd.com/challenges/food-recognition-benchmark-2022/dataset_files)
## [Food 101](https://www.kaggle.com/datasets/dansbecker/food-101?resource=download)
## [UEC FOOD 256](http://foodcam.mobi/dataset256.html)

## Foods found in at least 2 datasets:
* croissant
* pancakes
* cheesecake
* pho
* brownie
* sashimi
* french fries
* pancake
* fried rice
* grilled salmon
* waffle
* apple pie
* sausage
* guacamole
* sushi
* hamburger
* hummus
* tiramisu
* nachos
* paella
* dumplings
* steak
* lasagna
* tacos
* muffin
* caesar salad
* risotto
* pizza
* bibimbap
* french toast
* hot dog
* miso soup
* takoyaki
* rice