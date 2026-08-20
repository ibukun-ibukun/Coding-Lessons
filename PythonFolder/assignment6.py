
username = "Ibukun"
password = "6nuKuBi7"
attempts = 3

print("Welcome. You have 3 attempts to log in.")

while True:
    user = input("Username: ").strip()
    pswd = input("Password: ").strip()
    
    attempts = attempts - 1
    
    if user != username:
        print(f"Incorrect username. You have {attempts} attempts left.")

    elif pswd != password: 
        print(f"Incorrect password. {attempts} attempts left.")

    elif user == username and pswd == password:
        print(f"Access Granted. Welcome back {username}!")
        break

    if attempts == 0:
        print("Too many failed attempts. Account Locked.")
        break

        