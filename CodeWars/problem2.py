"""
                                -----------------
                                | Code War      |
                                | Problem 2     |
                                -----------------
Tags: [Arrays, Strings, Regular Expression]

Write a function that accepts an array of 10 integers(between 0 and 9), that returns a string of those numbers in the
form of a phone number

Example:
    createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890

"""


def createPhoneNumber(numbers):
    if len(numbers) != 10 or any(not (0 <= n <= 9) for n in numbers):
        raise ValueError("Input must be an array of 10 integers between 0 and 9")

    phoneNumber = "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)
    return phoneNumber


# Example Usage
print(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
