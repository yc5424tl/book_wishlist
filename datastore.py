# coding=utf-8
import os
import json
from book import Book

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

separator = '^^^'  # a string probably not in any valid data relating to a book

book_list = []
counter = 0


def setup():
    """ Read book info from file, if file exists. """

    global counter

    try:
        with open(BOOKS_FILE_NAME) as json_file_to_read:
            make_book_list(json.load(json_file_to_read))
    except FileNotFoundError:
        # First time program has run. Assume no books.
        pass

    try:
        with open(COUNTER_FILE_NAME) as f:
            try:
                counter = int(f.read())
            except:
                counter = 0
    except:
        counter = len(book_list)


def shutdown():
    """Save all data to a file - one for books, one for the current counter value, for persistent storage"""

    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass  # Ignore - if directory exists, don't need to do anything.

    with open(BOOKS_FILE_NAME, 'w') as target_output_file:
        json.dump(make_output_data(), target_output_file)

    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(counter))


def get_books(**kwargs):
    """ Return books from data store. With no arguments, returns everything. """

    global book_list

    if len(kwargs) == 0:
        return book_list

    if 'read' in kwargs:
        read_books = [book for book in book_list if book.read == kwargs['read']]
        return read_books


def add_book(book):
    """ Add to db, set id value, return Book"""

    global book_list

    book.id = generate_id()
    book_list.append(book)


def generate_id():
    global counter
    counter += 1
    return counter


def set_read(book_id, read):
    """Update book with given book_id to read. Return True if book is found in DB and update is made, False otherwise."""

    global book_list

    for book in book_list:

        if book.id == book_id:
            book.read = True
            return True

    return False  # return False if book id is not found

    # TODO - this can just return book.read


def make_book_list(data):
    """ turn the string from the file into a list of Book objects"""

    global book_list

    for title in data:
        book_list.append(Book(title, data.get(title.get('author')), data.get(title).get('id'), data.get(title.get('read'))))


def make_output_data():
    """ create a string containing all data on books, for writing to output file"""

    global book_list

    data_to_output_dict = {}

    for book in book_list:
        data_to_output_dict[book.title] = dict(author=book.author, id=book.id, read=book.read)

    return data_to_output_dict


def test_read_json_load_data():
    # check json dump

    with open(BOOKS_FILE_NAME) as json_file_to_read:
        input_data_dict = json.load(json_file_to_read)
        for book_dict in input_data_dict:
            print(book_dict.keys())
