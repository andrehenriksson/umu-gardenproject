import random
class Plant:
    def __init__(self, plant_name):
        self.name = plant_name
        self.plant_yield = random.random() 

class Vegetable(Plant):
    def __init__(self, plant_name):
        super().__init__(plant_name)

class FruitTree(Plant):
    def __init__(self, plant_name):
        super().__init__(plant_name)
    