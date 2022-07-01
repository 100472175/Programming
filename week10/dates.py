class Date:
    def __init__(self, day: int, month: str, year: int):
        """ This magic method is used to declare the attributes of the class """
        # Thee are the fields or attributes of the class
        if day < 31:
            self.day = day
        else:
            raise ValueError('Error while introducing a number, number to high')
        if year != 0:
            self.year = year
        else:
            raise ValueError('Valid years are only positive integer numbers ')
        months_name = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                       'november', 'december')

        self.month = month
        """else:
            raise ValueError('The month has to be in the months list:' + months_name)
        month_days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
                      'August': 31, 'September': 30, 'October': 31,
                       'November': 30, 'December': 31}"""

        if self.year % 4 == 0 and (self.year & 100 != 0 and self.year % 400 == 0):
            self.leap_year = True
        else:
            self.leap_year = False
        self.leap_year: bool

    def __str__(self):
        """This is the method that return when executing the print"""
        return self.month + ' ' + str(self.day) + ', ' + str(self.year)

    def __repr__(self):
        """This is the method that is invoked when typed into the terminal"""
        return self.month + ' ' + str(self.day) + ', ' + str(self.year)

    def __eq__(self, other):
        # To compare two elements instead of by address
        result = (self.day == other.day and self.month == other.month and self.year == other.year)

    #  A method has at least one parameter, called "self"
    def print_date(self):
        """
        :return: a string with he month, date and year
        """
        return self.month + ' ' + str(self.day) + ', ' + str(self.year)
