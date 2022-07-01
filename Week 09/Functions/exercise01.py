import random
# List of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
# List of all symbols available
symbols = ['!', '"', '·', '$', '%', '&', '/', '(', ')', '=', '?', '¿', '|', '@', '#', '¢', '∞', '¬', '÷', '“', '”', '≠',
           '´', 'œ', 'æ', '€', '®', '†', '¥', 'ø', 'π', 'å', '∫', '∂', 'ƒ', '', '™', '¶', '§', '~', 'Ω', '∑', '©', '√',
           'ß', 'µ', '+', '-', ',', '.', ';', ':', '_']


def rng_psswrd():
    """ Length between 8 and 12 characters
    1 upper case, 1 symbol, 1 number, but could be more.
    """
    password_list = []
    password = ''
    n = 0
    pswd_len = random.randrange(length[0], length[1])
    for i in range(pswd_len):
        password_list.append(str(letters[random.randrange(len(letters))]))
    num_num = int(random.randrange(len(password_list)))
    for i in range(num_num):
        password_list[random.randrange(len(password_list))-1] = random.randint(0, 9)
    sym_num = int(random.randrange(len(password_list)))
    for i in range(sym_num):
        password_list[random.randrange(len(password_list))-2] = symbols[random.randrange(len(symbols))]
    upp_num = int(random.randrange(len(password_list)))
    for i in range(upp_num):
        position = random.randrange(len(password_list))
        while type(password_list[position]) != str:
            position = random.randrange(len(password_list))
        password_list[position] = password_list[position].upper()

        while type(password_list[n]) != str:
            n += 1
        password_list[n] = password_list[n].capitalize()


    for e in password_list:
        password += str(e)
        password.replace("'", '')
        password.replace(',', '')

    return password


length = [8, 12]
password = rng_psswrd()
print(password)