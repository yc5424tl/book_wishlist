""" coding=utf-8 """


class Book:
    """ Represents one book in a user's list of books"""

    NO_ID = -1
    NO_RATING = -1

    def __init__(self, title, author, id_num=NO_ID, read=False, rating=NO_RATING, date_read=None):
        """Default book is unread, and has no ID or rating. """
        self.title = title
        self.author = author
        self.read = read
        self.id = id_num
        self.rating = rating
        self.date_read = date_read

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_id(self, id_num):
        self.id = id_num

    def get_title(self):
        return self.title

    def set_rating(self, rating):
        self.rating = rating

    def __str__(self):
        read_str = 'no'
        if self.read:
            read_str = 'yes'

        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        rating_str = self.rating
        if self.rating == -1:
            rating_str = "N/A"

        template = 'id: {} Title: {} Author: {} Read: {} Rating: {} Date Read: {}'

        return template.format(id_str, self.title, self.author, read_str, rating_str, str(self.date_read))

    def __eq__(self, other):

        return self.title == other.title and \
               self.author == other.author and\
               self.read == other.read and\
               self.id == other.id and\
               self.date_read == other.date_read and \
               self.rating == other.rating
