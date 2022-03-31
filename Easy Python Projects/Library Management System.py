class Library:
    
    def __init__(self, listOfBooks):
        self.books =  listOfBooks


    def displayAvailableBooks(self):
        print('\nBooks available in this Library are :-\n')
        for book in self.books:
            print(book)


    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f'You have been issued {bookName}, Kindly handle with care and return it within time.')
            self.books.remove(bookName)
        else:
            print(f'Sorry, {bookName} has already been issued to someone else, Please wait until it is returned.')

    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f'Thank You for returning {bookName}, Hope you enjoyed reading it.')

class Student:

    def requestBook(self):
        self.book = input('Enter the name of the book you want to borrow : ')
        return self.book

    def returnBook(self):
        self.book = input('Enter the name of the book you want to return : ')
        return self.book

centralLibrary = Library(['Java', 'Let us C', 'Python', 'SQL', 'Power BI'])
shubham = Student()

while True:
    welcome_message ='''
    ***** WELCOME TO CENTRAL LIBRARY *****

    Please choose from the below options :-
    1) Display available Books
    2) Issue a book
    3) Add / Return a book
    4) Exit the Library

    '''
    print(welcome_message)
    
    choice = int(input('Enter your choice : '))

    if choice == 1:
        centralLibrary.displayAvailableBooks()
    
    elif choice == 2:
        centralLibrary.borrowBook(shubham.requestBook())

    elif choice == 3:
        centralLibrary.returnBook(shubham.returnBook())

    elif choice == 4:
        print('Thank You for choosing Central Library.')
        exit()

    else :
        print('Invalid Choice')

    