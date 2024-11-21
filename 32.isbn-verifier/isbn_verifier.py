def is_valid(isbn):
    isbn = isbn.replace("-","")
    if len(isbn) != 10:
        return False
    result = 0
    try:
        for i in range(0, len(isbn)):
            if isbn[i] == 'X' and i == 9:
                result += 10 * (10-i)
                continue
            result += int(isbn[i]) * (10-i)
    except:
        return False
    if result % 11 == 0:
        return True
    return False
