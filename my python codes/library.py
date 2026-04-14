class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1
        print(f"Book added: {book_name}")

    def show_books(self):
        if self.books:
            print("Books in the library:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")
        else:
            print("No books in the library.")

    def get_no_of_books(self):
        return self.no_of_books


if __name__ == "__main__":
    # Create a library instance
    library = Library()

    # Add books
    library.add_book("Python Programming")
    library.add_book("Data Structure with C Programming")
    library.add_book("Java Programming")
    library.add_book("C Programming")

    # Show all books
    library.show_books()

    # Get number of books
    print(f"\nTotal number of books: {library.get_no_of_books()}")

    print("\nNow stop the program and rerun it to see that the books are not saved.")
    print("now execute the prohrwam " \
    "")
    print("hteh function willl be eduted olesae enter the ills" \
    "")















x = "nitesh"
print(x[::-1])















