import time

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow_book(self):
        if not self.borrowed:
            self.borrowed = True
            return f"You borrowed {self.title} by {self.author}"
        else:
            return f"This book {self.title} by {self.author} is already borrowed!"

class Library:
    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.books = []
        self.load_books()

    def load_books(self):
        raise NotImplementedError

    def show_books(self):
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book.title} by {book.author}")

class MainBranchLibrary(Library):
    def __init__(self):
        super().__init__('Main Branch')

    def load_books(self):
        with open("mainbranch_books.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                title, author = line.strip().split(',')
                self.books.append(Book(title, author))

class SubBranchLibrary(Library):
    def __init__(self):
        super().__init__('Sub Branch')

    def load_books(self):
        with open("subbranch_books.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                title, author = line.strip().split(',')
                self.books.append(Book(title, author))

main_library = MainBranchLibrary()
sub_library = SubBranchLibrary()

libraries = [main_library, sub_library]

while True:
    for idx, lib in enumerate(libraries, 1):
        print(f"{idx}. {lib.branch_name}")
    library_choice = int(input("Choose a library (Enter number or 0 to exit): "))

    if library_choice == 0:
        print("Goodbye!")
        break

    selected_library = libraries[library_choice-1]
    selected_library.show_books()

    book_choice = int(input("Which book would you like to borrow? (Enter number or 0 to go back): "))

    if book_choice == 0:
        continue

    print(selected_library.books[book_choice-1].borrow_book())
