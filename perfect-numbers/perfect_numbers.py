def aliquot_sum(number):
    """ Calculate divisors and return sum of them.
    
    :param number: int a positice integer
    :return: int sum of divisors of the number
    """
    divisors_sum = 0
    for num in range(1, number):
        if number % num == 0:
            divisors_sum += num
    return divisors_sum

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number > 0:
        a_sum = aliquot_sum(number)
        if a_sum == number:
            return "perfect"
        if a_sum > number:
            return "abundant"
        return "deficient"
    else:
         raise ValueError("Classification is only possible for positive integers.")
