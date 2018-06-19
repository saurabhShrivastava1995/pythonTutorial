myFile = open("data.txt", "r")
line = myFile.read()
myFile.close()
print(line)
user_input = input("Kaa naam baatey bauaaa ?? ")

myFile = open("data.txt", "w")
myFile.write(user_input)
myFile.close()
