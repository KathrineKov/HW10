class Book:
    def __init__(self, title, author, year, price, stoplist=False):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist

    def get_info(self):
        return "Author: " + self.author + ", Title: " + self.title + ", Year: " + str(self.year) + ", Price: $" + str(self.price) + ", Stoplist: " + str(self.stoplist)

    def find_most_expensive(books):
        if len(books) == 0:
            return None
        most_expensive = books[0]
        for book in books:
            if book.price > most_expensive.price:
                most_expensive = book
        return most_expensive

    def set_stoplist(self, value):
        self.stoplist = value

    def censor(self, author_name, value):
        if self.author == author_name:
            self.stoplist = value