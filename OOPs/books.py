# Define a class to represent a Book
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, Price: ${self.price}"

# Define a class to represent a Bookstore
class Bookstore:
    def __init__(self):
        self.inventory = []

    def add_book(self, book):
        if self.find_book(book.title):  # Check if the book is already in the inventory
            print(f"{book.title} is already in the inventory.")
        else:
            self.inventory.append(book)  # Only add the book if it's not a duplicate
            print(f"Added {book.title} to the inventory.")


    def display_books(self):
        if not self.inventory:
            print("No books in the inventory.")
        else:
            for book in self.inventory:
                print(book)

    def find_book(self, title):
        for book in self.inventory:
            if book.title == title:
                return book
        return None

    def sell_book(self, title):
        book = self.find_book(title)
        if book:
            self.inventory.remove(book)
            print(f"Sold {book.title}")
        else:
            print(f"{title} not found in the inventory.")


# Create a bookstore instance
my_bookstore = Bookstore()

# Add books to the inventory
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
book2 = Book("1984", "George Orwell", 8.99)

my_bookstore.add_book(book1)
my_bookstore.add_book(book2)

# Display available books
my_bookstore.display_books()

# Sell a book
my_bookstore.sell_book("1984")

# Try to sell a book not in inventory
my_bookstore.sell_book("Moby Dick")

# Display the remaining books
my_bookstore.display_books()

