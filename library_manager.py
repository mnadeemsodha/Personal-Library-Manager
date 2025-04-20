import os
import json

# File to save/load the library
LIBRARY_FILE = "library.txt"

# Load library from file if it exists
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a new book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }

    library.append(book)
    print("✅ Book added successfully!")

# Remove a book by title
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found.")

# Search for books by title or author
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    query = input("Enter search text: ").strip().lower()
    matches = []

    for book in library:
        if (choice == "1" and query in book["title"].lower()) or \
           (choice == "2" and query in book["author"].lower()):
            matches.append(book)

    if matches:
        print("\nMatching Books:")
        for i, book in enumerate(matches, 1):
            display_book(book, i)
    else:
        print("❌ No matching books found.")

# Display a single book
def display_book(book, index=None):
    read_status = "Read" if book["read"] else "Unread"
    prefix = f"{index}. " if index else ""
    print(f"{prefix}{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# Display all books
def display_all_books(library):
    if not library:
        print("📚 Your library is empty.")
        return
    print("\nYour Library:")
    for i, book in enumerate(library, 1):
        display_book(book, i)

# Show statistics
def display_statistics(library):
    total = len(library)
    if total == 0:
        print("📊 No books to show statistics.")
        return
    read_count = sum(1 for book in library if book["read"])
    percent_read = (read_count / total) * 100
    print(f"\n📈 Total books: {total}")
    print(f"✅ Percentage read: {percent_read:.1f}%")

# Menu system
def main():
    library = load_library()
    while True:
        print("\n📚 Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("📁 Library saved to file. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
