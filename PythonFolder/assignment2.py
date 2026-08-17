#name = 'ibukun'

#print(name)
#print(name.upper())
#print(name.lower)

#name2 = 'peter sam'
#print(name2.title())

#data = input("What is your name: ")

#print(data.strip())

#ASSIGNMENT

fullname = input ("enter your full name: ")
nickname = input("enter your nickname: ").strip()

clean_name = fullname.strip()

print("======================================")
print("           NAME FORMATTER             ")
print("--------------------------------------")
print("Original:              " + clean_name)
print("Uppercase:             " + clean_name.upper())
print("Lowercase:             " + clean_name.lower())
print("Titlecase:             " + clean_name.title())
print("Nickname:              " + nickname, "" + clean_name)
print("Characters:            " + str(len(clean_name)))
                  
length = len(clean_name)
if length < 15:
    print("Name Length:           Shorter than 15 characters")
else:
    print("Name Length:           Longer than 15 characters")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
  