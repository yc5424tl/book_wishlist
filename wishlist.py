#Main program

import book
import datastore
import file_io
import ui


def handle_choice(choice):

    choice_dict = {
        '1': show_unread,
        '2': show_read,
        '3': update_book_read,
        '4': add_new_book,
        '5': delete_a_book,
        '6': edit_book_title,
        '7': search_book,
        '8': edit_read_date_by_title,
        'q': quit_program,
    }

    function_call = choice_dict.get(choice)

    if function_call is None:
        ui.message('Invalid Selection, Try Again.')
    else:
        return function_call()
    # Thanks to https://www.pydanny.com/why-doesnt-python-have-switch-case.html


def search_book():
    """ Searches for a book in the wishlist and read lists """
    search_title = ui.get_title()
    search = datastore.search_books(search_title)
    ui.message('Book: ' + str(search))


def edit_read_date_by_title(updated_read_to_true=False, updated_title=None):

    target_title = updated_title

    if not updated_read_to_true:
        target_title = ui.get_title()

    if datastore.check_for_book_existence_in_system(target_title):
        if datastore.get_read_by_title(target_title):
                date_read = ui.get_date_read()
                datastore.set_date_read(target_title, date_read)
                datastore.set_read(target_title, set_to=False)


def edit_book_title():
    """ Edits a title of a book """
    edit_book = ui.get_title()
    ui.message("New title: ")
    new_title = input("")
    datastore.edit_title(edit_book, new_title)


def delete_a_book():
    """ Deletes a book """
    del_book = ui.get_title()

    if datastore.delete_book_by_title(del_book):
        ui.message('Book deleted: ' + str(del_book))
    else:
        ui.message('No Match Found for ' + str(del_book))


def show_unread():
    """Fetch and show all unread books"""
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    """Fetch and show all read books"""
    read = datastore.get_books(read=True)
    ui.show_list(read)


def update_book_read():
    """ Get choice from user, edit datastore, display success/error"""

    book_title = ui.get_title()
    mark_as = ui.get_read_update_type()
    if datastore.set_read(book_title, mark_as):
        ui.message('Successfully updated')
        rating = ui.get_rating_info()    #todo move rating to own method
        datastore.set_rating(book_title, rating)
        if mark_as:
            edit_read_date_by_title(updated_read_to_true=True, updated_title=book_title)
    else:
        ui.message('Book id not found in database')


def edit_book_rating():
    target_book_title = ui.get_title()

    if not datastore.check_for_book_existence_in_system(target_book_title):
        ui.message('No Match Found for Title: {}'.format(target_book_title))

    else:
        target_book_rating = ui.get_rating_info()
        datastore.set_rating(target_book_title, target_book_rating)


def add_new_book():
    """Get info from user, add new book"""
    title_and_author = ui.get_new_book_info()
    new_book = book.Book(title_and_author[0], title_and_author[1])
    datastore.add_book(new_book)
    ui.message('Book added: ' + new_book.get_title())
    warn_if_previously_read(new_book.title)


def quit_program():
    """Perform shutdown tasks"""
    prepared_data = datastore.make_output_data()
    file_io.update_data_sources(prepared_data, datastore.counter)
    ui.message('Bye!')


def warn_if_previously_read(title):
    if datastore.get_read_by_title(title):
        ui.warn_title_read_previously(title)


def start():

    list_data = file_io.build_list_data()

    if list_data is not None:
        datastore.import_data(list_data)

    counter_data = file_io.build_counter_data()

    if counter_data is None:
        datastore.counter = len(datastore.book_list)
    else:
        datastore.counter = counter_data


def main():

    start()

    quit_command = 'q'
    user_choice = None

    while user_choice != quit_command:
        user_choice = ui.display_menu_get_choice()
        handle_choice(user_choice)


if __name__ == '__main__':
    main()
