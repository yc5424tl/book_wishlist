""" coding=utf-8 """

import operator

from book import Book

book_list = []
counter = 0


def edit_title(title, new_title):
    """ Edits the title of a book within the wishlist. Edits any duplicate books as well. """

    for book in book_list:
        if book.title == title:
            book.set_title(new_title)

    sort_list()


def edit_rating(target_title, rating):
    """ Sets the rating for any book in the wishlist whose title matches target_title. """

    for book in book_list:
        if book.title == target_title:
            book.set_rating(rating)


def search_books(title):
    """ Returns a book from the data store, otherwise returns not found if not within the data store. """

    for book in book_list:
        if book.title == title:
            return book

    return "Not Found"


def get_books(**kwargs):
    """ Return books from data store. With no arguments, returns everything. """

    if len(kwargs) == 0:
        return book_list

    if 'read' in kwargs:
        return [book for book in book_list if book.read == kwargs['read']]


def delete_book_by_title(name):
    """ Removes a book from the book list. Also removes any duplicate books."""

    title_deleted = False

    for book in book_list:
        if book.title == name:
            book_list.remove(book)
            title_deleted = True

    sort_list()
    return title_deleted


def sort_list():
    """ Sorts books by title """

    book_list.sort(key=operator.attrgetter("title"), reverse=False)


def add_book(book):
    """ Adds a book object to the wishlist. """

    book.id = generate_id()
    book_list.append(book)
    sort_list()


def generate_id():
    """ Increments the counter used to produce unique book IDs. """

    global counter
    counter += 1
    return counter


def set_read(book_id, set_to=True):
    """ Update Book w/ book_id to read=True(default), return True. Returns False if book not found, or 'read' already desired Bool."""

    for book in book_list:

        if (book.id == book_id) and (book.read is not set_to):
            book.read = set_to
            return book.read

    return False  # if book id is not found


def import_data(data_dict):
    """ Instantiating book objects from data stored as (k, v) = (title, {author, id, read, rating}) in the the dict 'data'. """

    global book_list

    for title in data_dict:
        book_list.append(
            Book(title,
                 data_dict.get(title).get('author'),
                 data_dict.get(title).get('id'),
                 data_dict.get(title).get('read'),
                 data_dict.get(title).get('rating')))


def make_output_data():
    """ Store data in a dict with (k, v) = (title, {author, id, read}).  """

    global book_list

    data_to_output_dict = {}

    for book in book_list:
        data_to_output_dict[book.title] = dict(author=book.author, id=book.id, read=book.read, rating=book.rating)

    return data_to_output_dict


def query_read_by_title(title):
    """ Takes a book's title as argument, returns true only if 'read is True' for given title. """

    global book_list

    for book in book_list:
        if book.title == title:
            return book.read

    return None


def check_for_book_existence_in_system(title_to_query):
    """ Returns Boolean for if a title is stored book_list. """

    for book in book_list:
        if book.title == title_to_query:
            return True
    return False
