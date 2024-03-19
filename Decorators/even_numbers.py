def even_numbers(function):

    def wrapper(numbers):

        result = function(numbers)
        return [el for el in result if el % 2 == 0]

    return wrapper
