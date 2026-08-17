
mood = input("How are you feeling? (happy,sad,tired,bored,stressed): ").lower().strip()
energy_level = int(input("what is your energy level from 1 to 10 "))
time = input("What time of the day is it?(morning,afternoon,night): ").lower().strip()

if mood == "happy":
    if energy_level >=5 and energy_level <=10:
        if time == "morning" or "afternoon":
            print ("you seem happy! Go on a walk!")
        elif time == "night":
            print("You seem happy! watch a movie!")
    elif energy_level <5 and energy_level >=0:
        if time == "morning" or "afternoon":
            print ("Try drinking tea/coffee/water")
        elif time == "night":
            print("Try reading a book")
    else:
        print("Sorry this isn't part of the options,please try again later")

if mood == "sad":
    if energy_level >= 5 and energy_level <=10:
        if time == "morning" or "afternoon" :
            print("Take a walk")
        elif time == "night":
            print("Journal your thoughts")
    elif energy_level < 5 and energy_level >=0:
        if time == "morning" or "afternoon" :
            print("Listen to motivating music")
        elif time == "night":
            print("Avoid stressful tasks")
    else:
        print("Sorry this isn't part of the options,please try again later")

if mood == "tired":
    if energy_level >= 5 and energy_level <=10:
        if time == "morning" or "afternoon":
            print("Do some exercise")
        elif time == "night":
            print("It is time to sleep")
    if energy_level < 5 and energy_level >=0:
        if time == "morning" or "afternoon" :
            print("do some meditation")
        elif time == "night":
            print("Watch a movie")

    else:
        print("Sorry this isn't part of the options,please try again later")

if mood == "bored":
    if energy_level >= 5 and energy_level <=10: 
        if time == "morning" or "afternoon":
            print("Engage in a task")
        elif time == "night":
            print("Journal your thoughts")
    if energy_level < 5 and energy_level >=0:
        if time == "morning" or "afternoon" :
            print("Do a task that you have been postponing")
        elif time == "night":
            print("Watch a movie")
    else:
        print("Sorry this isn't part of the options,please try again later")
        
if mood == "stressed":
    if energy_level >= 5 and energy_level <=10:
        if time == "morning" or "afternoon":
            print("Do not eat heavy meals")
        elif time == "night":
            print("Drink some tea/coffee/water")
    if energy_level < 5 and energy_level >=0:
        if time == "morning" or "afternoon" :
            print("Get some rest")
        elif time == "night":
            print("Meditate")


"""
I am done!!!!!!!!!!!!!!!
QUESTIONS
If you noticed i put this:
else:
print("Sorry this isn't part of the options,please try again later")
after all the if statements but it was only the last one that wworked the way i wanted. 


        """
        



                    




