
contacts = [
    ["Annie", "0903 333 4467"],
    ["Bob", "0702 894 5635"],
    ["Ibukun", "0803 387 2350"]
]

def add_contact(contacts, name, number):
    for contact in contacts:
        if contact[0] == name:
            print("Contact already exists.")
            return 
            
    contacts.append([name, number])
    print("Contact added!")
    
def view_contacts(contacts):
    if len(contacts) == 0:
        print("There is no one in your contacts.")
    else:  
        print("YOUR CONTACT LIST:")
        for number, contact in enumerate(contacts, 1):
            print(f"{number}. Name: {contact[0]} \nNumber: {contact[1]}")

def find_contact(contacts, name):
    for contact in contacts:
        if contact[0] == name:
            return contact
    return None

def remove_contact(contacts, name):
    found = find_contact(contacts, name)
    if found:
        contacts.remove(found)
        print("Contact removed!")
    else:
        print("This contact does not exist.")

def update_contact(contacts, name, new_number):
    find_list = find_contact(contacts, name)
    if find_list:  
        find_list[1] = new_number
        print("Name number has been updated!")
    else:
        print("Contact not found")    

while True: 
    print("\nWhat would you like to do?")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Remove a contact")
    print("5. Quit")
    print("6. Update a contact (number)")

    user_choice = input("\nYour choice (1-6): ")

    if user_choice == "1":
        ask_for_name = input("Name: ")
        ask_for_number = input("Number: ")
        add_contact(contacts, ask_for_name, ask_for_number)
        
    elif user_choice == "2":
        view_contacts(contacts)
        break

    elif user_choice == "3":
        name = input("Search for: ")
        #name1, number = find_contact(contacts, name)  
        contact = find_contact(contacts, name)
        if contact:
            print(f"Contact Found: {contact[0]}| {contact[1]} ")
        else:
            print("Contact not found")

    elif user_choice == "4":
        name = input("What would you like to remove?: ")
        remove_contact(contacts, name)

    elif user_choice == "5":
        print("Thank you for using the Contact App. \nSee you next time.")    
        break

    elif user_choice == "6":
        name = input("Name: ")
        new_number = input("Enter the new number: ")
        update_contact(contacts, name, new_number)

    else:
        print("Please pick a number from 1-6.")   






