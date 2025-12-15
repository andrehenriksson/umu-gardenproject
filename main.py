
from file_handler import FileHandler

GARDEN_DATA_FILE = "data/gardendata.json"

def init_file_handler(garden_data_file):
    """Creates a show_runner

    Parameters
    ----------
    garden_data_file : str
        Path to JSON file.
    """

    file_handler = FileHandler(garden_data_file)
    return file_handler.garden

def print_menu():
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
    print("\n")

if __name__ == "__main__":
    #print_menu()

    garden_object = init_file_handler(GARDEN_DATA_FILE)

#    print(garden_object)
    print_menu()

    while(True):
        user_command = input("Please choose an option (type m to see the menu): ").lower().strip()
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
                    print(plant_name["name"])
            elif user_command == 'v':
                print('Adding vegetable...')
            elif user_command == 'f':
                print('Adding fruit tree...')
            elif user_command == 'h':
                print('Harvesting garden...')
            elif user_command == 'c':
                print('Caring for garden...')
            elif user_command == 'p':
                print('Adding pest...')
        else:
            print('Invalid command, please try again. Type m to see the menu.')