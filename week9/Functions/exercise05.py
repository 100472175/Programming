def correct_upper_case(sentence: str):
    """

    :param sentence: Sentence to capitalize
    :return: sentence, correctly capitalized
    """

    correct = ''
    correct += sentence[0].upper()
    for i in range(1, len(sentence)):
        # The second letter of the string will be added plain
        if i == 1:
            correct += sentence[i]
        # If the letter is preceded by something and a "." or a "?" or a "!", it will be capitalize
        elif sentence[i - 2] == '.' or sentence[i - 2] == '!' or sentence[i - 2] == '?':
            correct += sentence[i].upper()
        # If the letter is preceded by a space and followed by a space, it will be capitalized
        elif i+1 <= len(sentence) and sentence[i] == "i" and sentence[i - 1] == ' ' and sentence[i + 1] == ' ':
            correct += sentence[i].upper()
        # If the construction is I followed by apostrophe, "'", the i will be capitalized
        elif i+1 <= len(sentence) and [i-1] == ' ' and sentence[i] == 'i' and sentence[i+1] == "'":
            correct += sentence[i].upper()
        # the rest of the letters that do not satisfy the characteristics to be capitalized will be added without
        # modifications
        else:
            correct += sentence[i]

    return correct


sent = input('What is the sentence you want to capitalize: \n')
print(correct_upper_case(sent))
