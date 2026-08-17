
cart = []

def add_item(cart, name, price):
    for item in cart:
        if item[0].lower() == name[0].lower():
            print("That item is already in the cart.")
            return None 
        else:
            cart.append([name, price])
            print("Item has been added!")
            return None

def view_cart(cart):
    if len(cart) == 0:
        print("Your cart is empty")
    else:
        for number, item in enumerate(cart, 1):
            print(f"{number}. {item[0]}:       ₦{item[1]}") 

def get_total(cart):
    total_price = 0
    for item in cart:
        total_price += item[1]
    return total_price

def print_receipt(cart):
    
    if len(cart) == 0:
        print("There is nothing in your cart.")
    else:
        print("-------------------------------")
        print("          YOUR RECEIPT         ")
        print("------------------------------ ") 
        view_cart(cart)
        print(f"Total:           ₦{get_total(cart)}")
        print("Thank you for shopping with us, please have a nice day.")

while True:
    print("\nWhat would you like to do?")
    print("1. Add item")
    print("2. View cart")
    print("3. Print receipt and quit")
    user_choice=input("\nYour choice: ")

    if user_choice == "1":
        name = input("Item name: ")
        price = int(input("Price: "))
        add_item(cart, name, price)
    elif user_choice == "2":
        view_cart(cart)
    elif user_choice == "3":
        print_receipt(cart)
        break
    else:
        print("please choose a number from 1-3.")    

