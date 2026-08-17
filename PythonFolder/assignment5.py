
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
print(f"Age:                      {age}".title())
print(f"Favourite Subject:        {subject}".title())
''
if prefer == "morning" or "mornings":
    print("Vibe:                     Early Bird")
elif prefer == "night" or "nights":
    print("Vibe:                     Night Owl")

print(f"When Bored:               {bored}".title())
print(f"Friends Say:              {friends}".title())
print("------------------------------------------------")
print("             PERSONALITY  SUMMARY               ")
print("------------------------------------------------")

if prefer == "morning" and bored == "go out" and friends == "outgoing":
    print("You like fresh starts and prefer to go out with your" 
          "friends instead  of dying of boredom at home. Your" 
           "friends are lucky to have you around!")    



