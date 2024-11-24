import argparse

# Initialize the ArgumentParser object
parser = argparse.ArgumentParser(description="A simple argparse example.")

# Add arguments
parser.add_argument('name', type=str, help="Your name")
parser.add_argument('age', type=int, help="Your age")
parser.add_argument('--greet', action='store_true', help="If set, the program will greet you.")

# Parse arguments
args = parser.parse_args()

# Access the arguments
print(f"Name: {args.name}")
print(f"Age: {args.age}")

# Optional argument handling
if args.greet:
  print(f"Hello, {args.name}! You are {args.age} years old.")