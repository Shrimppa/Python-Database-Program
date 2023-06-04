import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('serviceAccountKey.json')

firebase_admin.initialize_app(cred, {'databaseURL': 'https://shrimppadatabaseproject-default-rtdb.firebaseio.com/'})

def show_data():
    ref = db.reference('item_catalogue')
    print(ref.get())

def add_data():

    reference_to_input = (input("Enter the the file path for the data: ")) # For example desserts/icecream would be turned into item_catalogue/desserts/icecream

    reference = 'item_catalogue/' + reference_to_input

    ref = db.reference(reference)

    key_to_input = (input("Enter what you want the key for the data to be: "))

    data_to_input = (input("Enter the data you want to input: "))
    
    print()

    ref.update({key_to_input : data_to_input})

def remove_data():

    reference_to_input = (input("Enter the the file path for the data: ")) # For example desserts/icecream would be turned into item_catalogue/desserts/icecream

    key_to_input = (input("Enter the key for the data you want to be deleted: "))

    reference = 'item_catalogue/' + reference_to_input + '/' + key_to_input

    ref = db.reference(reference)
    
    print()

    ref.delete()

def update_data():

    reference_to_input = (input("Enter the the file path for the data: ")) # For example desserts/icecream would be turned into item_catalogue/desserts/icecream

    key_to_input = (input("Enter the key for the data you want to change: "))

    data_to_input = (input("Enter the data you want to input: "))

    reference = 'item_catalogue/' + reference_to_input + '/' + key_to_input

    ref = db.reference(reference)
    
    print()

    ref.delete()
    
    updated_reference = 'item_catalogue/' + reference_to_input

    updated_ref = db.reference(updated_reference)

    updated_ref.update({key_to_input : data_to_input})

def get_choice():

    choice = 0
    
    while choice < 1 or choice > 6:
        choice = int(input("\nIf you want to see the menu input 6. Otherwise choose between options 1-5: "))
        print()

    return choice

def print_menu():

    print(
    f"Welcome to the database program!\n"
    + "__________________________________\n"
    + "1. Show data from database\n"
    + "2. Add data to database\n"
    + "3. Remove data from database\n"
    + "4. Update data in database\n"
    + "5. Quit program\n"
    )

def main():

    print_menu()

    choice = 6
    
    while choice != 5:
        choice = get_choice()

        if choice == 1:
            show_data()
        if choice == 2:
            add_data()
        if choice == 3:
            remove_data()
        if choice == 4:
            update_data()
        if choice == 5:
            quit
        if choice == 6:
            print_menu()

if __name__ == "__main__":
    main()