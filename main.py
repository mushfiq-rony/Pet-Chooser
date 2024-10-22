import pymysql.cursors
from credentials import *  # Import your database credentials

class Pet:
    def __init__(self, name, age, owner_name, animal_type):
        self.name = name            # Private attribute
        self.age = age
        self.owner_name = owner_name
        self.animal_type = animal_type

    # Getter and Setter for Name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Getter and Setter for Age
    def get_age(self):
        return self.age

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.age = age
        else:
            raise ValueError("Age must be a positive integer")

    # Getter and Setter for Owner's Name
    def get_owner_name(self):
        return self.owner_name

    def set_owner_name(self, owner_name):
        self.owner_name = owner_name

    # Getter and Setter for Animal Type
    def get_animal_type(self):
        return self.animal_type

    def set_animal_type(self, animal_type):
        self.animal_type = animal_type

    # String representation to print pet's information
    def __str__(self):
        return (f"{self.get_name()}, the {self.get_animal_type()}. "
                f"{self.get_name()} is {self.get_age()} years old. "
                f"{self.get_name()}'s owner is {self.get_owner_name()}.")




def connect_to_database():
    """Establish connection to the MySQL database."""
    try:
        connection = pymysql.connect(host=hostname,
                                     user=username,
                                     password=password,
                                     db=database,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        exit()


def fetch_pets(connection):
    """Fetch the list of pets from the database and return them as a list of Pet objects."""
    query = '''
    select
        pets.name,
        pets.age,
        owners.name as 'owner_name',
        types.animal_type
    from pets
    join owners
        on pets.owner_id = owners.id
    join types
        on pets.animal_type_id = types.id;
    '''

    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    pets = []
    for row in rows:
        pet = Pet(row['name'], row['age'], row['owner_name'], row['animal_type'])
        pets.append(pet)

    return pets


def display_pets(pets):
    """Display the list of pets."""
    print("\nPlease choose a pet from the list below:")
    for idx, pet in enumerate(pets, 1):
        print(f"[{idx}] {pet.name}")
    print("[Q] Quit")


def get_user_choice(pets):
    """Prompt the user to choose a pet and handle their input."""
    while True:
        choice = input("\nChoice: ").strip()

        if choice.lower() == 'q': # code for quitting.
            print("Goodbye!")
            exit()

        try:
            choice = int(choice)
            if 1 <= choice <= len(pets):
                return choice - 1
            else:
                print("Invalid choice. Please choose a valid number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number or 'Q' to quit.")


def main():
    """Main program loop."""
    connection = connect_to_database()

    while True:
        pets = fetch_pets(connection)  # Get pets from the database
        display_pets(pets)  # Show pets list to the user

        choice = get_user_choice(pets)  # Get the user's choice
        chosen_pet = pets[choice]  # Get the chosen pet

        print(f"\nYou have chosen {chosen_pet}.")  # __str__ method automatically called

        # Prompt the user to press ENTER to continue or Q to quit
        while True:
            input_prompt = input("\nPress [ENTER] to continue or [Q] to quit: ")
            if input_prompt == "":
                break  # Exit the loop if just Enter is pressed
            elif input_prompt.lower() == "q":
                print("Goodbye!")
                exit()  # Exit the program
            else:
                print("")


if __name__ == "__main__":
    main()
