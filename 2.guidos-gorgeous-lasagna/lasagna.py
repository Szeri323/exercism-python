"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate time needed to preaper lasagna.
    
    :param number_of_layers: int - the number of layers we want in our lasagna.
    :return: int - time needed to prepare our lasagna (in minutes) derived from 'PREPARATION_TIME'.
    
    Function that takes lasagna layer's and return time we need to prepare it based on the 'PREPARATION_TIME'.
    """
    
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ Calculate total time spent on cooking.
    
    :param number_of_layers: int - the numebr of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed baking time.
    :return: int - total time elapsed (in minutes) spent on preparing and cooking.
    
    Function that takes two integers representing the lasgna layers and time elapsed on baking as an arguments and calculates total time spent on cooking in minutes.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time