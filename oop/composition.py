class StoryBook : 
    #class variable
    no_of_books = 0
    discount = 0.5

    #instance variable
    def __init__(self, name, price, author_name, author_born, publishing_year, no_of_pages):
        self.name = name
        self.price = price
        self.author_name = author_name
        self.author_born = author_born
        self.publishing_year = publishing_year
        self.no_of_pages = no_of_pages
        StoryBook.no_of_books += 1

    
    #regular method
    def get_book_info(self):
        return (f'The Book name {self.name} has been published on {self.publishing_year} and pages {self.no_of_pages}.')
    
    #regular method
    def get_author_info(self):
        return (f'The author {self.author_name} and he was born {self.author_born}')
    
    #regular method
    def apply_discount(self):
        return self.price - self.price*self.discount
    
    #class method 01
    @classmethod
    def set_discount(cls,discount):
        cls.discount = discount

    #class method 02
    @classmethod
    def book_info_from_string(cls,book_string):
        name, price, author_name, author_born, publishing_year, no_of_pages = book_string.split(',')
        return cls(name, price, author_name, author_born, publishing_year, no_of_pages)

    #static method
    @staticmethod
    def get_publish_status(publishing_year):
        if publishing_year > 2000:
            print('This book is new published')
        else:
            print('This book is published more years ago')

book_1 = StoryBook('Hoimonti', 350,'Rabindranath' , 1564, 1620, 100)
book_2 = StoryBook('Sorola', 350,'Sukumar' , 1564, 1620, 100)

book_string = 'keyamah, 230, Dr. Abdullah jahangir, 1954, 2005, 250'

book_3 = StoryBook.book_info_from_string(book_string)

class Library:
    def __init__(self, book_list = None):
        if book_list is None:
            self.book_list = []
        else:
            self.book_list = book_list

    def get_all_books(self):
        for book in self.book_list:
            print(f'Name : {book.name}, Author : {book.author_name}')
    
    def add_book(self, book):
        self.book_list.append(book)

    def remove_book(self, book):
        self.book_list.remove(book)

public_library = Library()

public_library.add_book(book_1)
public_library.add_book(book_2)
public_library.add_book(book_3)
public_library.get_all_books()
public_library.remove_book(book_3)
public_library.get_all_books()