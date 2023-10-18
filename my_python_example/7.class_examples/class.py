class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow_book(self):
        if not self.borrowed:
            self.borrowed = True
            print(f"You borrowed {self.title} by {self.author}")
        else:
            print("This book is already borrowed!")

library = [Book("Harry Potter", "J.K. Rowling"), Book("Lord of the Rings", "J.R.R. Tolkien")]

for i, book in enumerate(library, 1):
    print(f"{i}. {book.title} by {book.author}")

choice = int(input("Which book would you like to borrow? (Enter number): "))
library[choice-1].borrow_book()
