def is_isogram(string):
    string = string.lower()
    letters = dict()
    for letter in string:
        if letter == "-" or letter == " ":
            continue
        if letter in letters:
            return False
        else:
            letters[letter] = 1
    return True
