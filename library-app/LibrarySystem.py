class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def display(self):
        status = "Issued" if self.is_issued else "Not Issued"
        return f"\n{self.book_id}\t{self.title}\t{self.author}\t{status}"


class Library:

    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = int(input("Enter book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        self.books.append(book)

        return "Book added successfully"

    def display_books(self):
        if not self.books:
            return "No books found"

        print(f"\nID\tTitle\tAuthor\tStatus")
        print("----------------------------------")

        for book in self.books:
            print(book.display())

    def issue_book(self):
        book_id = int(input("Enter Book ID To Issue Book: "))

        for book in self.books:
            if book.book_id == book_id:

                if not book.is_issued:
                    book.is_issued = True
                    print("Book Issued Successfully")
                else:
                    print("Book Already Issued")

                return

        print("Book Not Found")

    def return_book(self):
        book_id = int(input("Enter Book ID To Return Book: "))

        for book in self.books:
            if book.book_id == book_id:

                if book.is_issued:
                    book.is_issued = False
                    print("Book Returned Successfully")
                else:
                    print("Book Was Not Issued")

                return

        print("Book Not Found")

    def search_book(self):
        keyword = input("Enter Id or Title to search Book: ")
        found = False

        for book in self.books:
            if str(book.book_id) == keyword or book.title.lower() == keyword.lower():
                print(book.display())
                found = True

        if not found:
            print("Book Not Found")