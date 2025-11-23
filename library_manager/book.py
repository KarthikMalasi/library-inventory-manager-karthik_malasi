class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} | {self.author} | {self.isbn} | {self.status}"

    def to_line(self):
        return f"{self.title}|{self.author}|{self.isbn}|{self.status}\n"

    @staticmethod
    def from_line(line):
        title, author, isbn, status = line.strip().split("|")
        return Book(title, author, isbn, status)

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        self.status = "available"

    def is_available(self):
        return self.status == "available"
