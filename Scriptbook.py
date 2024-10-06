from Library import Book

books = [
    Book("A", "A1", 2021, 10),
    Book("B", "A2", 2022, 15.50),
    Book("C", "A3", 2023, 7, True)
]

for book in books:
    print(book.get_info())

most_expensive_book = Book.find_most_expensive(books)
if most_expensive_book is not None:
    print("\nMost Expensive Book:")
    print(most_expensive_book.get_info())

author_to_censor = "A3"
new_stoplist_value = False
for book in books:
    book.censor(author_to_censor, new_stoplist_value)

print("\nBooks After Censorship:")
for book in books:
    print(book.get_info())