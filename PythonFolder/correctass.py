
questions = [
        ["What does def do in python?", ["Defines a variable", "Defines a function", "deletes a file", "Displays output"], '2'],
        ["Which method adds an item to the end of the list?", [".insert()",".push()", ".append()",".add()"], '3'],
        ["What does return do in a function?", ["Prints a value","Ends the program", "Sends a value back", "Creates a loop"], '3']
    ] 
def ask_question(question, options):
    print(f"{question}")    
    for i, option in enumerate(options, 1):
        print(f"{i}.  {option}")
    pick_option = input("Please pick an option: ")
    return pick_option 

def check_answer(user_answer, answer):
    if user_answer == answer:
        return True
    else:
        return False

def show_score(score, total):    
    print(f"Your score is: {score} out of {total}.")
    if score == total:
        print("Excellent! You really know programming!")
    elif score < total:
        print("I know you can do better.")
    elif score == 0:
        print("You need to study more...")   

score = 0

for question, options, answer in questions:
    result = ask_question(question, options)
    user_answer = check_answer(result, answer)
    if user_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer is {answer}")  

show_score(score, len(questions))


   

         
       
