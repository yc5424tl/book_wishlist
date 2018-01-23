import json
import os

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')



def build_list_data():


    try :
        with open(BOOKS_FILE_NAME) as json_file_to_read:
            return json.load(json_file_to_read)
    except FileNotFoundError:
        return None # First time program has run. Assume no books.



def build_counter_data():
    """ Retrieve Counter Data from File """

    count = 0

    try:
        with open(COUNTER_FILE_NAME) as f:

                if count == 0:
                    pass

                else:
                    count = int(f.read())

                return count

    except IOError:
        return None


def update_data_sources(data_to_write):
    """Save all data to a file - one for books, one for the current counter value, for persistent storage"""

    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass # Ignore - if directory exists, don't need to do anything.

    with open(BOOKS_FILE_NAME, 'w') as target_output_file:
        json.dump(data_to_write, target_output_file)

    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(counter))
