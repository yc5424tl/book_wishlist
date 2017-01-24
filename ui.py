from book import Book


def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show unread books (wishlist)
        2. Show books that have been read
        3. Mark a book as read
        4. Add book to wishlist
        5. Search for a book
        6. Edit a title or author
        7. Delete a book
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


def ask_for_book_id():

    ''' Ask user for book id, validate to ensure it is a positive integer '''

    while True:
        try:
            id = int(input('Enter book id:'))
            if id >= 0:
                return id
            else:
                print('Please enter a positive number ')
        except ValueError:
            print('Please enter an integer number')


def get_new_book_info():

    ''' Get title and author of new book from user '''

    title = input('Enter title: ')
    author = input('Enter author: ')
    return Book(title, author)


def message(msg):
    '''Display a message to the user'''
    print(msg)


def get_search_term():
    search_term = input("Please enter a title or author keyword: ")
    return search_term


def ask_what_to_edit():
    response = input("Do you wish to edit the Author or Title? Enter 1 for Author or 2 for Title: ")
    while response != "1" and response != "2":
        response = input("That wasn't a 1 or 2, please try again.\nDo you wish to edit the Author or Title? Enter 1 for Author or 2 for Title: ")
    if response == "1":
        response = "author"
    elif response == "2":
        response = "title"
    return response

def ask_what_to_delete_by():
    search_term = input("Please enter a title or author keyword: ")
    return search_term


def get_new_value():
    new_value = input("What is the new value? ")
    return new_value
