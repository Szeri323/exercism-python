def rotate(text, key):
    new_s = ""
    for letter in text:
        if(ord(letter) >= 97 and ord(letter) <= 127):
            new_s += chr((ord(letter)-97 + key) % 26+97)
        elif(ord(letter) >= 65 and ord(letter) <= 90):
            new_s += chr((ord(letter)-65 + key) % 26+65)
        else:
            new_s += letter
    return new_s