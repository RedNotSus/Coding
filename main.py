list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
import random #import random module
randomnum = random.choice(list1) 
print("Welcome to the Jiayang App, Please sign in below!")
user = input("Please enter your JID number ")
password = input("Please enter your password ")
if user == ("1"):
    print("Account found. Welcome back Jiayang!")
    print("Please select an option below:")
    print("1. View your Balance")
    print("2. Check your messages")
    optionj = input("3. Use a app ")
    if optionj == ("1"):
        print("Your balance is 9999999 BIL")
    elif optionj == ("2"):
        print("You have no messages")
    elif optionj == ("3"):
        print("Please select an option below:")
        print("1. Guess a number")
        game = input("2. Password Generator")
        if game == ("1"):
            print("You have chosen to guess a number")
            print("Please enter a number between 1 and 10")
            guess = int(input("Please enter your guess "))
            if guess == (randomnum):
                print("You have guessed the number correctly")
            else:
                print("You have guessed the number incorrectly, the number was " + str(randomnum))

        elif game == ("2"):
            print("You have chosen to generate a password")
            print("Please enter a length between 1 and 10")
            length = int(input("Please enter the length of the password "))
            password = ""
            for i in range(length):
                password += random.choice("abcdefghijklmnopqrstuvwxyz")
            print("Your password is " + password)


elif user == ("2"):
    print("Account found. Welcome back Michael!")
    print("Please select an option below:")
    print("1. View your Balance")
    print("2. Check your messages")
    optionm = input("3. Use a app ")
    if optionm == ("1"):
        print("Your balance is $100")
    elif optionm == ("2"):
        print("You have no messages")
    elif optionm == ("3"):
        print("Please select an option below:")
        print("1. Guess a number")
        game = input("2. Password Generator")
        if game == ("1"):
            print("You have chosen to guess a number")
            print("Please enter a number between 1 and 10")
            guess = int(input("Please enter your guess "))
            if guess == (randomnum):
                print("You have guessed the number correctly")
            else:
                print("You have guessed the number incorrectly, the number was " + str(randomnum))

        elif game == ("2"):
            print("You have chosen to generate a password")
            print("Please enter a length between 1 and 10")
            length = int(input("Please enter the length of the password "))
            password = ""
            for i in range(length):
                password += random.choice("abcdefghijklmnopqrstuvwxyz")
            print("Your password is " + password)    

else: 
    print("Wrong Username or password!") 
