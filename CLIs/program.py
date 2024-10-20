import argparse

parser = argparse.ArgumentParser(description="A random program that does something", add_help=True)

parser.add_argument('filename')

argument = parser.parse_args()

print(argument)