def days_in_month(month: int, year: int):
    """

    :param month: month between 1 and 12
    :param year: to see if i is a leap year
    :return:
    """
    num = 0
    if month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    num = 29
                else:
                    num = 28
            else:
                num = 29
        else:
            num = 28
    elif month % 2 != 0 and month <= 7:
        num = 31
    elif month % 2 != 0 and month > 7:
        num = 31
    else:
        num = 30

    return num


month = int(input('What month do you want ot know the date? (1-12): '))
year = int(input('From which year: '))
print('There are', days_in_month(month, year), 'days')
