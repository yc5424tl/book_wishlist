from book import Book

def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show unread books (wishlist)
        2. Show books that have been read
        3. Mark a book as un/read
        4. Add book to wishlist
        5. Delete book from wishlist
        6. Edit a book title from wishlist
        7. Search for a book
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice


def show_list(books):
    ''' Format and display a list of book objects'''

    if len(books) == 0:
        print ('* No books *')
        return

    for book in books:
        print(book)

    print('* {} book(s) *'.format(len(books)))


def get_title():
    """ Asks user for book title """
    book_title = input("Enter the Book Title ")
    return book_title

def warn_title_read_previously(book):
    print('System Shows the latest entry, {}, shares a title with a book that has already been marked as read. No changes to either have been made.'.format(book.title))

def ask_for_book_id():
    """ Ask user for book id, validate to ensure it is a positive integer """

    while True:
        try:
            query_id = int(input('Enter book id:'))
            if query_id >= 0:
                return query_id
            else:
                print('Please enter a positive number ')
        except ValueError:
            print('Please enter an integer number')


def get_new_book_info():

    """ Get title and author of new book from user """

    title = input('Enter title: ')
    author = input('Enter author: ')
    return Book(title, author)


def message(msg):
    """ Display a message to the user """
    print(msg)


def get_rating_info():
    """ Gets rating for a read book and ensures its within the acceptable range """
    rating = int(input("Enter a rating between 1-5: "))

    while rating < 1 | rating > 6:
        rating = int(input("Enter a number betweeen 1 and 5 for the rating: "))

    return rating

def get_read_update_type():

    while True:
        update_type = input('Enter 1 to mark as read. Enter 2 to mark as not read.')

        if int(update_type) == 1:
            update_type = True
            break
        elif int(update_type) == 2:
            update_type = False
            break

    return update_type