celebs = [
    ["Johnny Depp", "63", "He dropped out of school at 15"],
    ["Tiwa Savage", "46", "She has a degree in accounting"],
    ["Mindy Kaling", "46", "She produced 'Never Have I Ever'"]
]

def add_celeb(celebs, name, age, fact):
    for celeb in celebs:
        if celeb[0] == name:
            print("This celebrity already exists.")
            return
    celebs.append([name, age, fact])
    print(f"{name} added!")

def find_celeb(celebs, name):
    for celeb in celebs:
        if celeb[0] == name:
            return celeb[0], celeb[1], celeb[2]
        return None, None, None
    
def print_profile(name, age, fact):
    found = find_celeb(celebs, name)
    if found:
        print()
        print(f"Name: {name}\nAge: {age}\nFun Fact: {fact}")
    else:
        print("Celebrity not found.")

def show_all(celebs):
    if len(celebs) == 0:
        print("Your celebrity list is empty.")
    else:  
        print("YOUR CELEBRITY LIST:")
        for number, celeb in enumerate(celebs, 1):
            print(f"{number}. Name: {celeb[0]} \nAge: {celeb[1]}")

while True:
    print("1. Search for a celeb")
    print("2. Add a celeb")
    print("3. View all celebs")
    print("4. Quit")

    user_choice = input("\nYour choice: ")

    if user_choice == "1":
        name1 = input("Who are you looking for?: ").strip()
        name, age, fact = find_celeb(celebs, name1)
        if name is not None:
            print_profile(name, age, fact)
        else:
            print(f"{name1} not found.")    
    
            
    elif user_choice == "2":
        name = input("Who do you want to add? ")
        age = input("Enter the age: ")
        fact = input("Fun Fact: ")
        add_celeb(celebs, name, age, fact)

    elif user_choice == "3":
        show_all(celebs) 

    elif user_choice == "4":
        print("See you next time.....")
        break

    else:
        print("Please input a number from 1-4.")

