"""

number = [4, 5, 6]

a, b, c = number 

print(a, b, c)

e, f, g = [1, 2, 3]

print(e, f, g)



# without unpacking
student = ["amara", 85]
name = student[0]
score = student [1]
print(f"{name} scored {score}!")

# with unpacking
student = ["amara", 85]
name, score = student
print(f"{name} scored {score}!")

celebs = [
    ["Rema", 24, "He wrote Calm Down at 19"],
    ["Tems", 29, "She studied Economics before music"],
    ["Wizkid", 33, "He released his first album at 11"]
    ]
for name, age, fact in celebs:
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Fun Fact: {fact}")
print()


print("Loading", )
print(".....")

names = ["Amara", "Shrimp", "border"]

for name in names:
    print( name, end=" ")


def add(a, b):
    return a + b

result = add(3, 5)
print(result)    
"""  



a, i, j = [[7, 8], 6, 4]

print(a[0], i, j)