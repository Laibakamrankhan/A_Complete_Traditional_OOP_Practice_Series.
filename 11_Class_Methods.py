#Create a class Book with a class variable total_books. 
#Add a class method increment_book_count() to increase the count when a new book is added

class Book:
    total_books = 0 

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  

bk1 = Book("Harry Potter")
bk2 = Book("Atomic Habit")
bk3 = Book("Python for begninner")

print(f"Total books: {Book.total_books}")
