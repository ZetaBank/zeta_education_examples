import time  # 시간을 다루기 위해 time 모듈을 가져옵니다.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False
        self.borrowed_time = None  # 언제 빌려졌는지 시간을 기록하기 위한 변수 추가

    def borrow_book(self):
        current_time = time.time()  # 현재 시간을 가져옵니다.

        # 이미 빌린 상태이고, 10초가 지나지 않은 경우
        if self.borrowed and current_time - self.borrowed_time < 10:
            print(f"This book is already borrowed! Wait for {10 - (current_time - self.borrowed_time):.2f} seconds.")
            return

        if not self.borrowed:
            self.borrowed = True
            self.borrowed_time = current_time  # 빌릴 때의 시간을 기록합니다.
            print(f"You borrowed {self.title} by {self.author}")
        else:
            print("This book is available now!")
            self.borrowed = False  # 책을 다시 도서관에 돌려놓습니다.

library = [Book("Harry Potter", "J.K. Rowling"), Book("Lord of the Rings", "J.R.R. Tolkien")]

while True:  # 무한 반복해서 사용자 입력을 받습니다.
    for i, book in enumerate(library, 1):
        print(f"{i}. {book.title} by {book.author}")

    print("0. Exit")  # 종료 옵션 추가

    choice = int(input("Which book would you like to borrow or return? (Enter number): "))

    if choice == 0:
        print("Goodbye!")
        break
    elif 1 <= choice <= len(library):
        library[choice-1].borrow_book()
    else:
        print("Invalid choice! Try again.")
