import operator

from book import Book

book_list = []
counter = 0

def edit_title(title, new_title):
    """ Edits the title of a book within the wishlist. Edits any duplicate books as well """

    #TODO another candidate for moving to the book class
    for book in book_list:
        current_title = book.title
        if current_title == title:
            book.set_title(new_title)

    sort_list()


def add_rating(id, rating):
    """ Sets the rating of a read book """
    #todo this could be moved to book class
    global book_list

    for book in book_list:
        get_id = book.id
        if get_id == id:
            book.set_rating(rating)




def search_books(title):
    """ Returns a book from the data store, otherwise returns not found if not within the data store"""
    global book_list

    for book in book_list:
        if book.title == title:
            return book

    return "Not Found"   #TODO return 'None' here

def get_books(**kwargs):
    """ Return books from data store. With no arguments, returns everything. """

    global book_list

    if len(kwargs) == 0:
        return book_list

    if 'read' in kwargs:
        return [ book for book in book_list if book.read == kwargs['read'] ]



def delete_book_by_title(name):
    """ Removes a book from the book list. Also removes any duplicate books."""

    global book_list
    title_deleted = False

    for book in book_list:
        if book.title == name:
            book_list.remove(book)
            title_deleted = True

    sort_list()
    return title_deleted

def sort_list():
    """ Sorts books by title """
    global book_list

    book_list.sort(key=operator.attrgetter("title"), reverse=False)


def add_book(book):
    """ Add to db, set id value, return Book"""

    global book_list

    book.id = generate_id()
    book_list.append(book)
    sort_list()


def generate_id():
    global counter
    counter += 1
    return counter


def set_read(book_id, set_to=True):
    """ Update book with given book_id to read (default). Return True if book is found in DB and update is made,
        False otherwise."""
    #TODO this seems like it could be moved to the book class

    global book_list

    for book in book_list:

        if (book.id == book_id) and (book.read is not set_to):
            book.read = set_to
            return book.read

    return False # if book id is not found


def make_book_list(data):
    """ Iterated instantiation of book objects w/ attributes stored as (k, v) = (title, {author, id, read}) in the the dict 'data' """

    global book_list

    for title in data:
        book_list.append(Book(title, data.get(title.get('author')), data.get(title).get('id'), data.get(title.get('read'))))


def make_output_data():
    """ Store data in a dict with (k, v) = (title, {author, id, read})  """

    global book_list

    data_to_output_dict = {}

    for book in book_list:
        data_to_output_dict[book.title] = dict(author=book.author, id=book.id, read=book.read)

    return data_to_output_dict


def query_read_by_title(title):
    """Takes a book's title as argument, returns true only if 'read is True' for given title."""
    global book_list

    for book in book_list:
        if book.title == title:
            return book.read

    return False