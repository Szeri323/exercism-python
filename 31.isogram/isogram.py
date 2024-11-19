def is_isogram(string):
    string = string.lower()
    letters = dict()
    for letter in string:
        if letter == "-" or letter == " ":
            continue
        try:
            letters[letter]
        except KeyError:
            letters[letter] = 1
        else:
            return False
    return True
