#!python3
# while loop example again

while True:
    print("Who are you?")
    name = input()
    if name != "Joe":
        continue
    print("Hello, Joe. What is the password")
    password = input()
    if password == "swordfish":
        break
    print("Access Granted!")

