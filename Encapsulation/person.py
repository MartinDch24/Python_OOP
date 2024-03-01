class Person:

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_age(self) -> int:
        return self.__age

    def get_name(self) -> str:
        return self.__name
