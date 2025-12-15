class GardenContainer:
    def __init__(self, plants = None):
        if plants is None:
            plants = {}
        self.plants = plants

    def add_plant(self, plant):
        self.plants[plant.name] = plant

    def __str__(self):
        return f'The garden has {len(self.plants)} plants.'