import random

name = input("What is your name?: ")
gender = input("Are you a girl or a boy?: ").lower().strip()

locations = ["an abandoned cave","a lost city","an ice mmountain","a spooky forest","a volcano","a sunken ship"]
companions = ["a monkey with boots","a talking backpack","a mad scientist","a robot","a mysterious stranger","a wise old woman"]
challenges = ["solve a riddle","climb an abandoned tower","fix a puzzle","help a homeless girl","find a key","kill a dragon","decode a message"]
twists = ["it was all a dream","you misplace the reward","your companion backstabs you (literally)","the map was wrong","the companion disappears","it starts to rain"]

location = random.choice(locations)
companion = random.choice(companions)
challenge = random.choice(challenges)
whatday = random.randint(2,9)
days = random.randint(10,15)
reward = random.randint(100,800)

random.shuffle(twists)
twist = twists[0]


print("Your Adventure:")
print("                        ")
print(f"{name.title()} set off on a journey to {location}.")

if gender == "girl":
    print(f"Her companion for the trip was {companion}.")

elif gender == "boy":
    print(f"His companion for the trip was {companion}.")

else:
    print(f"Their companion for the trip was {companion}.")

print(f"On day {whatday} of the journey they had to {challenge} to move forward.")
print(f"The adventure lasted {days} days and the reward was {reward} gold coins")
if reward > 500:
    print("Wow! That is a big reward! I advice you share it with your companion... ")
print(f"But then - {twist}.")
print("                        ")
print("Run the program again for a new adventure!")

