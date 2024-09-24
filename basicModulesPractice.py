"""
======================================================================================================================
Author:                         {root@lonedevwolf}
Language:                       Python
Modules:                        os, sys
======================================================================================================================
[1]: Command-Line Argument:     The script prints the name of the script and any argument passed to it using "sys.argv"
[2]: Current Working Directory: It retrieves and prints the current working directory using "os.getcwd()".
[3]: Changing Directory:        It creates a new directory and changes the current working directory to this new
                                directory to this new directory using "os.makedirs() and os.chdir().
[4]: Environment Variable:      It gets and prints the value of the PYTHONPATH environment variable and sets a new
                                environment variable
[5]: File Operations:           It creates a new file, writes to it, and then reads from it.
"""
import os
import sys


def main():
    # Print the script name and commandline arguments
    scriptName = sys.argv[0]
    arguments = sys.argv[1:]
    print(f"Script Name: {scriptName}")
    print(f"Arguments: {arguments}")

    # Get and print the current Working Directory
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}")

    # Change the current Working Directory
    newDirectory = os.path.join(cwd, 'newFolder')
    os.makedirs(newDirectory, exist_ok=True)
    os.chdir(newDirectory)
    print(f"Changed working directory to: {os.getcwd()}")

    # Get and print an environment variable
    pythonPath = os.environ.get("PYTHONPATH: ", "Not Found")
    print(f"New Environment Variable: {pythonPath}")

    # Set a new environment variable
    os.environ["NEW_VAR"] = 'newValue'
    print(f"New Environment Variable: {os.environ["NEW_VAR"]}")

    # Create a new file and write to it
    filePath = os.path.join(newDirectory, 'example.txt')
    with open(filePath, 'w') as file:
        file.write("Hello Wolrd!!!!!!!!")
        print(f"Created and wrote to file: {filePath}")

    # Read from the file
    with open(filePath, 'r') as file:
        content = file.read()
        print(f"Read from file: {content}")


if __name__ == "__main__":
    main()
