def greet(name):
    print(f"Hello {name}")

name = "Ibukun" 

greet(name)

greet("Shalome")

greet("Messi")

my_contact = [
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
    
add_contact(my_contact, "Annie", "0903 859 4803")