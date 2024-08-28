# Клас, що використовує делегування для розширення функціональності книги
class LibraryBookInfo:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}"

# Перероблений клас LibraryBook, що використовує делегування
class LibraryBook:
    def __init__(self, title, author, publication_year):
        self.info = LibraryBookInfo(title, author, publication_year)
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

    def get_info(self):
        return self.info.get_info()

# Використання коду
book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(book.check_out())
print(book.check_out())
print(book.get_info())
