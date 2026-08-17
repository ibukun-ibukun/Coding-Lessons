
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b
    
def multiply(a,b):
    return a * b 

def divide(a,b):
    if b == 0:
        print("You cannot divide by zero.")
        return None
    else:
        return a/b
     
def mod(a,b):
    return a % b

def power(a,b): 
    return a ** b   

print("Welcome to the calculator!")
print("Enter an operator: ")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print("5. modulus")
print("6. power")
operator = input("Choose an operation (1-6): ")
if operator not in range(1,7):
    print("Invalid number!") 

no1 = float(input("Enter number 1: "))
no2 = float(input("Enter number 2: "))

if operator == "1":
    output = add(no1, no2)
    print(f"The answer is {output}")
elif operator == "2":
    output = subtract(no1, no2)
    print(f"The answer is {output}")
elif operator == "3":
    output = multiply(no1, no2)
    print(f"The answer is {output}")      
elif operator == "4":
    output = divide(no1, no2)
    print(f"The answer is {output}") 
elif operator == "5":
    output = mod(no1, no2)
    print(f"The remainder is {output}") 
elif operator == "6":
    output = power(no1, no2)
    print(f"The answer is {output}")     
else:
    print("Your number is invalid. Please enter a number between 1 and 7.")    




