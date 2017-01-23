import os
import datastore
import json  #store files in json format

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')


def setup():
    ''' Read book info from file, if file exists. '''

    global counter

    try:
        with open(BOOKS_FILE_NAME) as f:
            data = f.read()
            datastore.make_book_list(data)
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
        counter = len(datastore.book_list)


def shutdown():
    '''Save all data to a file - one for books, one for the current counter value, for persistent storage'''

    output_data = datastore.make_output_data()

    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass # Ignore - if directory exists, don't need to do anything.

    with open(BOOKS_FILE_NAME, 'w') as f:
        #f.write(output_data)
        json.dumps(output_data) # Saves data in json format
    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(counter))
        #json.dumps(counter)
