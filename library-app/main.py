from LibrarySystem import *

library = Library()

while True:
    print("\n====== Library Management System ======")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        print(library.add_book())

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        library.issue_book()

    elif choice == 4:
        library.return_book()

    elif choice == 5:
        library.search_book()

    elif choice == 6:
        print("Thank You! Library System")
        break

    else:
        print("Invalid choice")