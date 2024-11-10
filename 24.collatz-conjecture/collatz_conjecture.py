def process_number(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1
    
def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return 0
    for num in range(1,number+1):
        number = process_number(number)
        if number == 1:
            break
    return num
