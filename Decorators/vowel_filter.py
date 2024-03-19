def vowel_filter(function):
    vowels = ['a', 'e', 'u', 'i', 'o', 'y']

    def wrapper():
        result = function()
        return [el for el in result if el.lower() in vowels]
    return wrapper
