from inventory import LibraryInventory

inventory = LibraryInventory()

def menu():
    print("\n===== Library Inventory Manager =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

while True:
    menu()
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input!")
        continue

    if choice == 1:
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        inventory.add_book(title, author, isbn)
        print("Book added successfully!")

    elif choice == 2:
        isbn = input("Enter ISBN to issue: ")
        book = inventory.search_by_isbn(isbn)
        if book and book.issue():
            inventory.save_data()
            print("Book issued!")
        else:
            print("Book not available or already issued.")

    elif choice == 3:
        isbn = input("Enter ISBN to return: ")
        book = inventory.search_by_isbn(isbn)
        if book:
            book.return_book()
            inventory.save_data()
            print("Book returned!")
        else:
            print("Book not found.")

    elif choice == 4:
        for b in inventory.display_all():
            print(b)

    elif choice == 5:
        keyword = input("Enter title keyword: ")
        results = inventory.search_by_title(keyword)
        if results:
            for b in results:
                print(b)
        else:
            print("No matching book found.")

    elif choice == 6:
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
