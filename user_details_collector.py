from random import randint
import re


def initMessage():
    """
    This function returns a welcome message to the user
    """
    return("Welcome to HNG Tech!\nWe would need a few details from you.\nDo well to follow the instructions properly.\n")


def getUserObject(userObject):
    "This function takes in dictionary object userObject and returns a string, formatted with the object's properties"
    userid = userObject["userid"]
    firstName = userObject["firstName"]
    lastName = userObject["lastName"]
    email = userObject["email"]
    password = userObject["password"]

    return f"\nUser {userid} details\nFirst Name: {firstName}\nEmail Address: {email}\nLast Name: {lastName}\nPassword: {password}"


def getAllUsers(users):
    """
    This function uses the getUserObject function to print all users to the console
    """
    alluserDetails = "\nProgram Summary"
    for user in users:
        alluserDetails += f"\n{getUserObject(user)}"
    return alluserDetails


def validateNames(name, nameInString):
    """
    This function validates the first and last name and return the correct name when the user has inputed the correct name
    """
    while len(name) < 2:
        print(
            f"\nYour {nameInString} should be greater than two characters")
        name = input(
            f"Please input your {nameInString}: ")
        if len(name) >= 2:
            return name


def isValidEmail(email):
    """
    This function checks if an email address is valid
    """
    valid = re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if valid:
        return True
    else:
        return False


def correctEmail(email):
    """
    This function corrects an email address if it's invalid by continously asking the user to return a valid email
    """
    valid = isValidEmail(email)
    while not valid:
        print("Email address incorrect! Please, input a valid email of the form x@y.com")
        email = input("Please input your email address: ")
        valid = re.match(
            '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if valid != None:
            return email


def collectDetails(id):
    """
    This fucntion collects user details using the input global method
    """
    print(f"\nYou are user {id}")

    firstName = input("Please input your first name: ")
    if len(firstName) < 2:
        firstName = validateNames(firstName, "first name")

    lastName = input("Please input your last name: ")
    if len(lastName) < 2:
        lastName = validateNames(lastName, "last name")

    password = randomPasswordGen(firstName, lastName)

    email = input("Please input your email address: ")

    if not isValidEmail(email):
        email = correctEmail(email)

    userObject = {
        "userid": id,
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "password": password
    }

    print(f"Your password is {password}")

    acceptPassword = input("Do you accept this password? (yes or no)? ")

    if acceptPassword != "yes" and acceptPassword != "no":
        print("\nPlease, enter a valid response")
        acceptPassword = input("Do you accept this password? (yes or no)? ")

    if acceptPassword == "no":
        password = input(
            "Please choose a password with 7 characters or more: ")
        greaterThan7Characters = len(password) > 7

        while not greaterThan7Characters:
            print(
                "\nYour password is less than 7 characters.")
            password = input(
                "Please choose a password with 7 characters or more: ")
            if len(password) > 7:
                break
        userObject["password"] = password
        return userObject
    else:
        return userObject


def randomPasswordGen(firstName, lastName):
    """
    This function returns a random password by combining a user's first name, last name and a random string
    """
    randomStrSet = "1!a2@b3#c4$d5%^f6&g7*h89h30p"
    fiveLetterRandStr = ""
    for _ in range(5):
        fiveLetterRandStr += randomStrSet[int(
            randint(0, len(randomStrSet) - 1))]

    return firstName[0:2] + lastName[0:2] + fiveLetterRandStr


def runProgram():
    """
    This is the entry point of the program. It runs a bunch of functioins in the program and contains the loop which continously runs the program
    """
    print(initMessage())
    users = []
    keepRunning = True
    currentid = 1

    while keepRunning:
        currentUser = collectDetails(currentid)
        print(getUserObject(currentUser))
        users.append(currentUser)

        runAgain = input(
            "\nDo you want to run the program again? (yes or no): ")

        while runAgain != "yes" and runAgain != "no":
            print("\nPlease, enter a valid response")
            runAgain = input(
                "\nDo you want to run the program again? (yes or no)? ")
            if runAgain == "yes" or runAgain == "no":
                break

        if runAgain == "no":
            print(getAllUsers(users))
            print("\nGoodbye")
            keepRunning = False
        else:
            currentid += 1


runProgram()
