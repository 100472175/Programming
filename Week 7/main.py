# This is the function, stored into memory but not executed
def launching(countdown, success):
    """ This code simulates the launching of a rocket
     the countdown starts in 10
     @param countdown : the time for the countdown
     :param success if True the launching is successfull
    """
    if type(countdown) == int and countdown > 0 and type(success) == bool:
        print('Everything is ready for launching')
        for i in range(countdown, -1, -1):
            print(i)
        print('Launching...')
        if success:
            print('Huston, everything goes OK')
            print('Look, we are closer to the moon')
        else:
            print('Huston, we have problems')
            print('Returning to Earth immediately')
    else:
        print('The first parameter should be an integer')
        print('The second parameter should be a boolean')


# This is where the main program starts
launching(10, True)
