import json

from plant import (
    Vegetable,
    FruitTree,
)

from garden import GardenContainer

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)
class SaveHandler:
    def __init__(self, garden_data_file):
        self.garden_data_file = garden_data_file
    def _save_garden(self, garden):
        """Saves the garden data to a JSON file."""
        garden_data = []
        for plant in garden.plants.values():
            plant_data = {
                "name": plant.name,
                "class": "VEGETABLE" if isinstance(plant, Vegetable) else "FRUITTREE",
                "harvest_weeks": list(plant.harvest_weeks),
                "yields_per_week": plant.yields_per_week,
            }
            garden_data.append(plant_data)
        try:
            with open(self.garden_data_file, mode="w", encoding="utf-8") as out_file:
                json.dump(garden_data, out_file, indent=4)
        except IOError as e:
            print(f"Error writing to output file {self.garden_data_file}: {e}")
            raise

class FileHandler:
    def __init__(self, garden_data_file):
        self.garden = GardenContainer()
        self._read_json_input(garden_data_file, self._initialize_garden)

    def _read_json_input(self, json_file, init_method):
        """Reads the content of a json file and applies init_method to its content"""
        try:
            with open(json_file, mode="r", encoding="utf-8") as input_file:
                json_data = json.load(input_file)
            init_method(json_data)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading input file {input_file}: {e}")
            raise

    def _create_vegetable(self, entry):
        return Vegetable(
            plant_name=entry.get("name"),
            harvest_weeks=entry.get("harvest_weeks", []),
            yields_per_week=entry.get("yields_per_week", {}),
        )

    def _create_fruittree(self, entry):
        return FruitTree(
            plant_name=entry.get("name"),
            harvest_weeks=entry.get("harvest_weeks", []),
            yields_per_week=entry.get("yields_per_week", {}),
        )
    
    def _initialize_garden(self, garden_data):
        """Initializes character objects and adds them to the Play"""
        for entry in garden_data:
            garden_class = entry.get("class")
            if garden_class == "VEGETABLE":
                plant = self._create_vegetable(entry)
            elif garden_class == "FRUITTREE":
                plant = self._create_fruittree(entry)
            else:
                raise ValueError(f"Unknown plant class {garden_class}")
            self.garden.add_plant(plant)

    def writefile():
        # Writing to a new file (or overwriting an existing one)
        with open("my_file.txt", "w") as f:
            f.write("This is the first line.\n")
            f.write("This is the second line.\n")
            f.write("And this is the last line.")

        # Appending to an existing file
        with open("my_file.txt", "a") as f:
            f.write("\nAdding a new line to the end.")

        # Writing with string formatting
        name = "Alice"
        age = 30
        with open("user_data.txt", "w") as f:
            f.write(f"Name: {name}\n")
            f.write(f"Age: {age}\n")
            
    def readfile():
        #import json

        # Python dictionary
        data = {
            "name": "Alice",
            "age": 30,
            "isStudent": False,
            "courses": ["Math", "Science"]
        }

        # Serialize to JSON string
        json_string = json.dumps(data, indent=4) # indent for pretty-printing
        print("JSON String:")
        print(json_string)

        # Write to a JSON file
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
        print("\nData written to data.json")
