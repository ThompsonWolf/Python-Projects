print("[!] Data Structure and Algorithms in Python (DSA)")


class Developer:  
    # This is the construtor for the class. It is called whenever a Developer object is created.
    # The reference called "self" is created by Python and made to the space for the newly created object.
    # Python does this automatically for us but we have to "self" as the first parameter to the __init__ method (i.e the constructor).

    def __init__(self, name, age, typeOfDeveloper, programmingLanguage, speakLanguage):
        self.name = name
        self.age = age
        self.typeOfDeveloper = typeOfDeveloper
        self.programmingLanguage = programmingLanguage
        self.speakLanguage = speakLanguage

    # This is an accessor method that returns the speakLanguage stored in the object.
    # Notice that "self" is a parameter.
    # Every method has "self" as its first parameter.
    # The "self" parameter is a reference to the current object.
    # The current object appears on the left hand side of the dot (i.e the (.) when the method is called)

    def speak(self):
        return self.speakLanguage

    # Here is an accessor method to get the name of the Developer
    def getName(self):
        return self.name

    # This is another accessor method that uses the age information to return a string representing the age
    def age(self):
        return str(self.age)

    # This is a mutator method that change the speakText of the Developer object.
    def changeSpeakLanguage(self, language):
        self.speakLanguage = language







def main():
    web = Developer("Thompson", 24, "Website Developer", ["HTML/CSS/JS", "Django/Flask"], "Web is fun")
    mobile = Developer("Kyle", 25, "Mobile Developer", ["Kotlin", "Flutter"], "Mobile is Interactive and Interesting")
    game = Developer("Irene", 18, "Game Developer", ["C#", "C++", "Unreal Engine"], "Game Developers are cool guys")
    lowLevelNerds = Developer("Wolf", 24, "Low Level Developer", ["C", "Assembly", "Mathematics"], "We got the whole world in our hands")
    scriptKiddies = Developer("Mattison", 12, "BlackHat Hacker", ["Python", "Bash", "C/C++"], "Hacking is wild")

    print(web.name)
    print(mobile.getName())
    print(game.age)
    print(lowLevelNerds.programmingLanguage)
    print(scriptKiddies.speak())


if __name__ == "__main__":
    main()







