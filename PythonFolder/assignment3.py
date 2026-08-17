#DIFFERENCEW BTW STRINGS AND NUMBER
#A string is a character that is enclosed in a quotation mark
#the difference is shown below
"""
print("12"+"12")
print(12+12)

name = input("name-- ")
age = (input("age-- "))
print("Hello " + name + " you are " + age + " years old." )
"""

name= input("What is your name:  ").lower().strip()
age = int(input("How old are you? "))
subject = input("What is your favourite subject : ").lower().strip()
prefer = input("Do you prefer mornings or nights? ").lower().strip()
bored = input("What do you do when you are bored?(read/sleep/eat/go out/watch TV)").lower().strip()
friends = input("What would your friends describe in one word?: ").lower().strip()

print("================================================")
print("              YOUR DIGITAL PROFILE              ")
print("================================================")
print(f"Name:                     {name}".title())
print(f"Age:                      {age}")
print(f"Favourite Subject:        {subject}".title())
''
if prefer == "morning" or prefer == "mornings":
    print("Vibe:                     Early Bird")
elif prefer == "night" or prefer == "nights":
    print("Vibe:                     Night Owl")

print(f"When Bored:               {bored}".title())
print(f"Friends Say:              {friends}".title())
print("------------------------------------------------")
print("             PERSONALITY  SUMMARY               ")
print("------------------------------------------------")

if prefer == "morning" or prefer == "mornings" and bored == "go out" and friends == "outgoing":
    print("You like fresh starts and prefer to go out with your " 
          "friends instead  of dying of boredom at home. Your" 
          "friends are lucky to have you around!")

elif prefer == "morning" or "mornings" and subject == "math" or "maths" or"science":
    print("You are a focused and driven person. You like to get things done early and you take your work seriously.")

elif prefer == "night" or "nights" and bored == "watch TV":
    print("You are a chill and relaxed person.You know how to unwind and you never stress about the small things.")

elif bored == "eat" or "sleep" or "go out" and friends == "loyal":
    print("You are the dependable one of your friend group. You are basically always your friends' 'last hope'. People know that they can count on you no matter what")

elif bored == "go out" and subject == "history" or "science":
    print("You are a sight-seer at heart. You love exploring and trying out new things. You are the brave one of your group seeks adventure.")

elif friends == "creative" or subject == "art" or "music":
    print("You have a wild imagination ")

else:
    print("I am sure that you have a great personality but i can't really figure you out right now...Sorry.")