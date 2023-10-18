import time

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False
        self.borrowed_time = None

    def borrow_book(self):
        current_time = time.time()

        if self.borrowed and current_time - self.borrowed_time < 10:
            print(f"This book is already borrowed! Wait for {10 - (current_time - self.borrowed_time):.2f} seconds.")
            return

        if not self.borrowed:
            self.borrowed = True
            self.borrowed_time = current_time
            print(f"You borrowed {self.title} by {self.author}")
        else:
            print("This book is available now!")
            self.borrowed = False

class Library:
    def __init__(self):
        self.books = []
        self.storage_floor = {}

    def add_book(self, book):
        self.books.append(book)
        # 제목의 첫 알파벳을 기준으로 층을 할당
        if book.title[0].lower() >= 'g':
            self.storage_floor[book.title] = 3
        else:
            self.storage_floor[book.title] = 2

    def show_books(self):
        for i, book in enumerate(self.books, 1):
            floor = self.storage_floor[book.title]
            print(f"{i}. {book.title} by {book.author} (Stored in floor {floor})")

library = Library()
library.add_book(Book("Harry Potter", "J.K. Rowling"))
library.add_book(Book("Lord of the Rings", "J.R.R. Tolkien"))
library.add_book(Book("Gatsby", "F. Scott Fitzgerald"))

while True:
    library.show_books()

    print("0. Exit")

    choice = int(input("Which book would you like to borrow or return? (Enter number): "))

    if choice == 0:
        print("Goodbye!")
        break
    elif 1 <= choice <= len(library.books):
        library.books[choice-1].borrow_book()
    else:
        print("Invalid choice! Try again.")
