def is_pangram(sentence):
    sentence = sentence.lower()
    sentence = set(sentence)
    conter = 0
    for letter in sentence:
        if letter.isalpha():
            conter += 1
    if conter == 26:
        return True
    return False
