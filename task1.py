# This program remove all keys from the dictionary that have the specified value.

# Define a sample dictionary
my_dict = {
    'Bob': "Backend Engineer",
    'Mark': "Gangster",
    'Wolf': "Code Warlord",
    'Zorro': "Weapon Master"
}

def complex_delete(a_dictionary, value):
    # Create a list of keys to delete
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    
    # Delete the keys from the dictionary
    for key in keys_to_delete:
        del a_dictionary[key]
    
    return a_dictionary



# Call the function and specify the value to delete (e.g., the exact value of the dictionary)
complex_delete(my_dict, "Backend Engineer")

# Print the updated dictionary
print(my_dict)


