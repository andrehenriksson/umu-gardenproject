
from file_handler import FileHandler
import pest
import plant

GARDEN_DATA_FILE = "data/gardendata.json"

currentYear = 2024
currentWeek = 24
debug = False

def init_file_handler(garden_data_file):
    """Creates a garden object from a JSON file.

    Parameters
    ----------
    garden_data_file : str
        Path to JSON file.

    Returns
    ----------
    garden : GardenContainer
        The initialized garden object.
    """
    file_handler = FileHandler(garden_data_file)
    return file_handler.garden

def print_menu():
    """Prints the menu options."""
    print("\n")
    print("Current Year:", currentYear)
    print("Current Week:", currentWeek)
    print("\n")
    print("Garden Manager menu:\n")
    print("s - show all plants (sorted alphabetically) and pests (sorted by week)\n")
    print("v - add vegetable")
    print("f - add fruit tree")
    print("h - harvest (list the yield for all plants in the garden)")
    print("c - care for garden")
    print("p - add pest")
    print("q - quit the program")
    print("m - show menu")
    print("set - set year and week")

    print("\n")

if __name__ == "__main__":
    #print_menu()

    garden_object = init_file_handler(GARDEN_DATA_FILE)

#    print(garden_object)
    print_menu()

    while(True):
        print("\n")
        print("-"*20)
        print("\n")
        user_input = input("Please choose an option (type m to see the menu): ").lower().strip()
        user_input_parts = user_input.split()
        user_command = user_input_parts[0].lower().strip()

        if len(user_input_parts) == 2 and user_command == 'debug':
            try:
                tmp_debug = str(user_input_parts[1].lower().strip())

                if tmp_debug in ['true', '1', 'yes']:
                    debug = True
                elif tmp_debug in ['false', '0', 'no']:
                    debug = False
                else:
                    print("Invalid debug value. Please enter true/false, 1/0, or yes/no.")
                    print("\n")
            except ValueError:
                print("Invalid input. Please enter a valid debug value.")
            continue

        if len(user_input_parts) == 3 and user_command == 'set':
            try:
                new_year = int(user_input_parts[1])
                new_week = int(user_input_parts[2])
                if new_year >= currentYear and 1 <= new_week <= 52:
                    currentYear = new_year
                    currentWeek = new_week
                    print(f"Date updated to Year: {currentYear}, Week: {currentWeek}")
                    print("\n")
                else:
                    print("Invalid year or week. Please ensure the year is not in the past and the week is between 1 and 52.")
                    print("\n")
            except ValueError:
                print("Invalid input. Please enter numeric values for year and week.")
            continue


        if len(user_input_parts) == 4 and user_command == 'p':
            try:
                pest_name = user_input_parts[1]
                affected_plant = str(user_input_parts[2].lower().strip())
                week_detected = int(user_input_parts[3])

                print(f"Adding pest: {pest_name}, Affected Plant: {affected_plant}, Week Detected: {week_detected}, type: {type(affected_plant)}")

                if affected_plant not in ["fruittree", "vegetable"]:
                    print("Invalid affected plant. It must be either 'FruitTree' or 'Vegetable'.")
                    continue
                if week_detected < 1 or week_detected > 52:
                    print("Invalid week detected. It must be between 1 and 52.")
                    continue

                new_pest = pest.Pest(pest_name, affected_plant, week_detected)
                garden_object.add_pest(new_pest)
            except ValueError as e:
                print(f"Error adding pest: {e}")
            continue

        if user_command in ['s', 'v', 'f', 'h', 'c', 'p', 'q', 'm']:
            if user_command == 'q':
                print("\n")
                print('Goodbye!')
                break
            elif user_command == 'm':
                print_menu()
            elif user_command == 's':
                for plant_name in sorted(garden_object.plants):
                    print(garden_object.plants[plant_name])
#                    print(plant_name["name"])
                for plant_name in sorted(garden_object.pests):
                    print(garden_object.pests[plant_name])
#                    print(plant_name["name"])
            elif user_command == 'v':
                print('Adding vegetable...')
                tmp_vegetable = plant.Vegetable("Vegetable1")
                garden_object.add_plant(tmp_vegetable)
            elif user_command == 'f':
                print('Adding fruit tree...')
                tmp_fruittree = plant.FruitTree("FruitTree1")
                garden_object.add_plant(tmp_fruittree)
            elif user_command == 'h':
                print('Harvesting garden...')
                total_yield = garden_object.harvest(currentYear, currentWeek, traceflag=debug)
                print(f'Total yield for week {currentWeek} of year {currentYear}: {total_yield}')
            elif user_command == 'c':
                print('Caring for garden...')
                garden_object.care_for_garden()
            elif user_command == 'p':
                print('Adding pest...')
                tmp_pest = pest.Pest("Pest1", "Vegetable", 12)
                garden_object.add_pest(tmp_pest)
        else:
            print('Invalid command, please try again. Type m to see the menu.')