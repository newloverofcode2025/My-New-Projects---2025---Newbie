from library import Library

def main():
    # Initialize the library
    library = Library("library.json")

    while True:
        print("\n=== Library Management System ===")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Display All Books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book(title, author, isbn)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter the ISBN of the book to remove: ")
            if library.remove_book(isbn):
                print("Book removed successfully!")
            else:
                print("Book not found.")

        elif choice == "3":
            query = input("Enter title, author, or ISBN to search: ")
            results = library.search_books(query)
            if results:
                print("\nSearch Results:")
                for book in results:
                    print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
            else:
                print("No matching books found.")

        elif choice == "4":
            books = library.get_all_books()
            if books:
                print("\nAll Books in Library:")
                for book in books:
                    print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
            else:
                print("The library is empty.")

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()