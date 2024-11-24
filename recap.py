import string

# Chaotic Function
def main():
    print("This program illustrates a chaotic function")
    x = int(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)


# main()

# Temperature Converter Function
def tempConverter():
    celsius = int(input("What is the Celsius temperature?: "))
    fahrenheit = 9.0 /5.0 * celsius + 32
    print(f"The temperature is {fahrenheit} degree Fahrenheit.")


# tempConverter()

# Text to Numbers
# A program to convert a textual message into a serial number, utilizing the underlyig ASCII encoding the message
def textToNumber():
    # Get the Message to ecode
    message = input("Please Enter your message: ")
    print("Here are the ASCII codes: ")
    # Loop through the message and print out the ASCII Characters
    for ch in message:
        print(">> : ", ord(ch))

# textToNumber()

# # A program to convert a sequence of ASCII numbers into a string of text
def numberToText():
    # Get the message to encode
    inString = input("Please enter the ASCII encoded message: ")

    # Loop through each substring and build ASCII message
    message = ""
    for numStr in inString:
        asciiNum = eval(numStr)             # convert digit string to a number
        message = message + chr(asciiNum)   # append character to message

        print("The decoded message is: ", message)


numberToText()



# Creating a funtion that generates a username
def genUsername():
    # Get users first and last names
    firstName = input("[!]: Please enter your First name (all lowercase): ")
    lastName = input("[!]: Please enter your Last names (all lowercase): ")

    # Concatenates first and initial with 7 characters of the last name
    uname = firstName[0] + lastName[:7]

    # Output the username
    print(f"Your generated username is : {uname}")


# genUsername()


# Creating a function that print the abbreviation of a month, given its number
def abbrMonth():
    # Months is used as lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    
    n = int(input("Enter a month number (1-12): "))
    # Compute starting position of month n in months
    pos = n-1 * 3

    # Grab the appropriate slice from months
    monthAbbrev = months[pos:pos+3]

    # print the result
    print(f"The month abbreviation is {monthAbbrev}.")



# abbrMonth()




























