import json
class Book:

    ''' Represents one book in a user's list of books'''

    NO_ID = -1

    def __init__(self, title, author, read=False, id=NO_ID, date_read = "unread", rating = "None"):
        '''Default book is unread, has no ID, and the rating is '''
        self.title = title
        self.author = author
        self.read = read
        self.id = id
        self.date_read = date_read
        self.rating = rating

    def set_id(self, id):
        self.id = id

    def __str__(self):
        read_str = 'no'
        if self.read:
            read_str = 'yes'

        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        template = 'id: {} Title: {} Author: {} Read: {} Date Read: {} Rating: {}'
        return template.format(id_str, self.title, self.author, read_str, self.date_read, self.rating)

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.read == other.read and self.id == other.id and self.date_read == other.date_read and self.rating == other.rating

    def set_rating(self, rating):
        self.rating = rating


''' Possible to make a JSON decoder too, think I'm missing something
to get that working. '''

def from_json(dictionary):
    b = Book('', '')
    b.__dict__ = dictionary
    return b

''' Encode = turn object into JSON '''
class BookEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__
