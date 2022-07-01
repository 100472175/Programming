class Date:
    def __init__(self, day: int, month: str, year: int):
        """ This magic method is used to declare the attributes of the class """
        # Thee are the fields or attributes of the class

        self.__month = month

        if day < 31:
            self.day = day
        else:
            self.day = 0
            raise ValueError('Error while introducing a number, number to high')
        self.year = year

        """else:
            raise ValueError('The month has to be in the months list:' + months_name)
        month_days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
                      'August': 31, 'September': 30, 'October': 31,
                       'November': 30, 'December': 31}"""

        """if self.year % 4 == 0 and (self.year & 100 != 0 and self.year % 400 == 0):
            self.leap_year = True
        else:
            self.leap_year = False
        self.leap_year: bool"""

    @property
    def year(self):
        """I return the attribute but with __ before """
        return self.__year

    @year.setter
    def year(self, year: int):
        if type(year) != int:
            raise TypeError('The year must be an integer')
        elif year != 0:
            self.__year = year
        else:
            raise ValueError('There is no 0 year! ')

    def __str__(self):
        """This is the method that return when executing the print"""
        return self.month + ' ' + str(self.day) + ', ' + str(self.year)

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        months_name = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                       'november', 'december')
        if type(month) != str:
            raise TypeError('The month must be a string')
        elif month.lower in months_name:
            self.__month = month
        else:
            raise ValueError()

    @property
    def leap_year(self):
        if (self.year % 4 == 0 and (self.year % 100 != 0)) or self.year % 400 == 0:
            return True



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


