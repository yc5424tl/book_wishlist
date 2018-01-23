#Main program

import datastore
import ui


def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        update_book_read()

    elif choice == '4':
        add_new_book()

    elif choice == '5':
        delete_a_book()

    elif choice == '6':
        edit_a_book()

    elif choice == '7':
        search_book()

    elif choice == 'q':
        quit_program()

    else:
        ui.message('Please enter a valid selection')

def search_book():
    """ Searches for a book in the wishlist and read lists """
    search_title = ui.get_title()
    search = datastore.search_books(search_title)
    ui.message('Book: ' + str(search))

def edit_a_book():
    """ Edits a title of a book """
    edit_book = ui.get_title()
    ui.message("New title: ")
    new_title = input("")
    datastore.edit_title(edit_book, new_title)

def delete_a_book():
    """ Deletes a book """
    del_book = ui.get_title()
    datastore.delete_book_by_title(del_book)
    ui.message('Book deleted: ' + str(del_book))


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

    book_id = ui.ask_for_book_id()
    mark_as = ui.get_read_update_type()
    if datastore.set_read(book_id, mark_as):
        ui.message('Successfully updated')
        rating = ui.get_rating_info()    #todo move rating to own method
        datastore.add_rating(book_id, rating)
    else:
        ui.message('Book id not found in database')


def add_new_book():
    """Get info from user, add new book"""
    new_book = ui.get_new_book_info()
    datastore.add_book(new_book)
    ui.message('Book added: ' + str(new_book))
    warn_if_previously_read(new_book.title)


def quit_program():
    """Perform shutdown tasks"""
    datastore.shutdown()
    ui.message('Bye!')

def warn_if_previously_read(title):
    if datastore.query_read_by_title(title):
        ui.warn_title_read_previously(title)

def main():

    datastore.setup()

    quit_command = 'q'
    user_choice = None

    while user_choice != quit_command:
        user_choice = ui.display_menu_get_choice()
        handle_choice(user_choice)


if __name__ == '__main__':
    main()
