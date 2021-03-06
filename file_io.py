""" coding=utf-8 """

import json
import os
from json import JSONDecodeError

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')


def build_list_data():
    """ Retrieves JSON data stored in target file. """

    try:
        with open(BOOKS_FILE_NAME) as json_file_to_read:
            return json.load(json_file_to_read)
    except FileNotFoundError:
        return None  # First time program has run. Assume no books.
    except JSONDecodeError:
        return {}


def build_counter_data():
    """ Retrieve JSON Counter Data from File. """

    try:
        with open(COUNTER_FILE_NAME) as f:
            return int(f.read())

    except IOError:
        return None


def update_data_sources(book_data, counter_data):
    """ Save all data in JSON format to 2 files - one for books, one for the current counter value, for persistent storage. """

    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass  # Ignore - if directory exists, don't need to do anything.

    with open(BOOKS_FILE_NAME, 'w') as target_output_file:
        json.dump(book_data, target_output_file)

    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(counter_data))
