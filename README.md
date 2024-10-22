# Pet Selection Program

This program connects to your personal "pets" database, reads pet data, and allows the user to interactively choose a pet from the list. Once a pet is selected, the program displays the pet's information and the pet's owner. 

## Features
- **Connect to MySQL Database**: The program connects to a MySQL database using `pymysql` to fetch the list of pets.
- **Pets Class**: Each pet is represented as an instance of the `Pets` class, stored in a separate file (`pets.py`).
- **Interactive User Selection**: The user can choose a pet from a numbered list and see its details.
- **Error Handling**: The program catches errors and displays user-friendly messages, ensuring smooth user experience.
- **Quit Option**: The user can exit the program by pressing 'Q' or 'q' at any time.

## How It Works
1. The program starts and connects to your "pets" database.
2. It reads data from the database and creates one instance of the `Pets` class for each pet listed.
3. The user is presented with a numbered list of pet names to choose from.
4. After selecting a pet by its number, the program prints detailed information about that pet.
5. If the user selects an invalid choice, a user-friendly error message is displayed, and the user is prompted to choose again.
6. The program continues running until the user presses 'Q' or 'q' to quit.


## Usage
1. Clone this repository to your local machine.
2. Open the project in PyCharm.
3. Ensure you have the necessary credentials for connecting to your database (place them in a `credentials.py` file).
4. Run the program, and follow the on-screen instructions.

## Requirements
- Python 3.12
- PyMySQL
- A MySQL database 

## Database Schema
Make sure your database has the following tables (example):
- **pets**: id, name, age, type_id, owner_id
- **owners**: id, name
- **types**: id, type_name

## Installation
1. Install required packages: "pymysql"

