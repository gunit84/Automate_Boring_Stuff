#!python3
# Test Python Example

passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()

print("Enter your password.")
typedPassword = input()

if typedPassword == secretPassword:
    print("Access Granted")
    if typedPassword == "12345":
        print("That password is one that someone puts on their luggage")
else:
    print("Access Denied")

