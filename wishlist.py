# Main program

import ui, datastore, fileIO
from book import Book


def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        new_book()

    elif choice == '5':
        search()

    elif choice == '6':
        edit()

    elif choice == '7':
        delete()

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')


def show_unread():
    '''Fetch and show all unread books'''
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    '''Fetch and show all read books'''
    read = datastore.get_books(read=True)
    ui.show_list(read)


def book_read():
    ''' Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()

    if datastore.set_read(book_id, True):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def new_book():
    '''Get info from user, add new book'''
    new_book = ui.get_new_book_info()
    if new_book != "null":
        datastore.add_book(new_book)
        ui.message('Book added: ' + str(new_book))


def search():
    search_results = []
    all_books = datastore.get_books()
    search_term = ui.get_search_term()
    for book in all_books:
        if search_term in book.title:
            search_results.append(book)
        elif search_term in book.author:
            search_results.append(book)

    print("Here's what I found:")
    ui.show_list(search_results)


def edit():
    id = ui.ask_for_book_id()
    to_edit = ui.ask_what_to_edit()
    new_value = ui.get_new_value()
    for book in datastore.book_list:
        if book.id == id:
            read = book.read
            title = book.title
            author = book.author
            if to_edit == 'author':
                datastore.book_list.remove(book)
                datastore.book_list.append(Book(title, new_value, read, id))
            elif to_edit == 'title':
                datastore.book_list.remove(book)
                datastore.book_list.append(Book(new_value, author, read, id))

    print("Successfully updated.")


def delete():
    id = ui.ask_for_book_id()
    for book in datastore.book_list:
        if book.id == id:
            datastore.book_list.remove(book)
            print("Successfully deleted.")


def check_book_in_system(title, author):
    for book in datastore.book_list:
        if book.author == author and book.title == title and book.read is True:
            return "read"
        elif book.author == author and book.title == title and book.read is False:
            return "unread"
        elif book.author != author or book.title != title:
            return False
    if len(datastore.book_list) == 0:
        return False


def quit():
    '''Perform shutdown tasks'''
    fileIO.shutdown()
    ui.message('Bye!')


def main():

    fileIO.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
