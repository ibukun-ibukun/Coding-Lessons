
import random
print("Welcome to the Guessing Game Arcade!")

name = input("What is your name?: ").lower().strip()
mode = input("Which mode shall we play? (easy, hard, chaos mode) ").lower().strip()

dramahints = ["Why are you even guessing that high?","Not even close,","Warmer... actually no. Ice Cold,","Tell me when you are done..."]
drama_hints = ["The number is embarrased for you,","Warmer,","Are you Bad at this or what?","Are you sure you know how to play this game?!"]
games = 0
wins = 0
while True:

    games += 1    


    if mode == "easy":
        print("I am thinking of a number between 1 and 20.")
        easy_guess = random.randint(1,20)
        attempts = 0

        while True:
            easy_user_guess = int(input("Your guess: "))
            attempts = attempts + 1

            if easy_user_guess > easy_guess:
                print("Too High!")

            elif easy_user_guess < easy_guess:
                print("Too Low!")
            
            elif easy_user_guess == easy_guess:
                wins = wins + 1
                print(f"Correct {name.title()}! You took {attempts} guesses to figure the number out!")
                break
                
    elif mode == "hard":
        print("WARNING: YOU ONLY HAVE 7 GUESSES")
        hard_guess = random.randint(1,50)
        attempts = 7

        print("I am thinking of a number between 1 and 50...")

        while True:
            hard_user_guess = int(input("Your guess: "))
            attempts = attempts - 1

            if hard_user_guess == hard_guess:
                print(f"Correct {name.title()}! You took {7-attempts} guesses to figure it out.")
                wins = wins + 1
                break

            elif attempts == 0 :
                print("You have run out of guesses.")
                print(f"The number was {hard_guess}. Better Luck next time {name.title()}..")
                break

            elif hard_user_guess > hard_guess:
                print("Too High!")
                print(f"You have only {attempts} guessesleft")

            elif hard_user_guess < hard_guess:
                print("Too Low!")
                print(f"You have only {attempts} guessesleft")

    elif mode == "chaos mode" or mode == "chaos":
        print("Alright-Chaos Mode !")
        chaos_guess = random.randint(1,100)
        
        attempts = 0

        print("I am thinking of a number between 1 and 100...")

        while True:
            chaos_user_guess = int(input("Your guess: "))
            attempts = attempts + 1
            if chaos_user_guess > chaos_guess:
                print(f"{random.choice(dramahints)} {name.title()}! ")

            if chaos_user_guess < chaos_guess:
                print(f"{random.choice(drama_hints)} {name.title()}! ")

            elif chaos_user_guess == chaos_guess:
                print("FINALLY! You have guessed the correct number!")
                print(f"You guessed {attempts} times to get this number.")
                wins = wins + 1
                break
    else:
        print("Invalid Mode. Choose between easy,hard and chaos")
        
    again = input("Play Again? Yes or No ").lower().strip()
                

    if again == "n":
        print(f"Games: {games} | Wins: {wins}")
        print(f"Bye {name.title()}!")
        break

    elif again == "y":
        print("Ok then.")
        mode = input("Which mode shall we play? (easy, hard, chaos mode) ").lower().strip()
            