from pymongo import MongoClient

# Connect to MongoDB (Replace with your Atlas URI if using cloud)
client = MongoClient("mongodb://localhost:27017/")  # Local MongoDB instance
db = client["library"]  # Create or switch to 'library' database
books_collection = db["books"]  # Create or switch to 'books' collection

# Function to Insert a Book
def insert_book(title, author, year, genre):
    book = {"title": title, "author": author, "year": year, "genre": genre}
    result = books_collection.insert_one(book)
    print(f"Book inserted with ID: {result.inserted_id}")

# Function to Update a Book
def update_book(title, new_data):
    result = books_collection.update_one({"title": title}, {"$set": new_data})
    if result.matched_count:
        print(f"Book '{title}' updated successfully.")
    else:
        print(f"Book '{title}' not found.")

# Function to Delete a Book
def delete_book(title):
    result = books_collection.delete_one({"title": title})
    if result.deleted_count:
        print(f"Book '{title}' deleted successfully.")
    else:
        print(f"Book '{title}' not found.")

# Function to Show All Books
def show_books():
    books = books_collection.find()
    for book in books:
        print(book)

# Sample Usage
if __name__ == "__main__":
    insert_book("The Alchemist", "Paulo Coelho", 1988, "Fiction")
    insert_book("Sapiens", "Yuval Noah Harari", 2011, "History")
    
    print("\n📚 Library Collection:")
    show_books()

    print("\n🔄 Updating 'The Alchemist'...")
    update_book("The Alchemist", {"year": 1993})

    print("\n🗑 Deleting 'Sapiens'...")
    delete_book("Sapiens")

    print("\n📚 Final Collection:")
    show_books()
