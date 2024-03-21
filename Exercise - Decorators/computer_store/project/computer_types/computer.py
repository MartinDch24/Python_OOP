from abc import ABC, abstractmethod
import re
from math import log2


class Computer(ABC):

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    @abstractmethod
    def available_processors(self):
        ...

    @property
    @abstractmethod
    def max_ram(self):
        ...

    @property
    def manufacturer(self):
        return self.__manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @staticmethod
    def power_of_two(ram: int):
        result = log2(ram)
        return result.is_integer()

    def configure_computer(self, processor: str, ram: int) -> str:
        computer_type = self.__class__.__name__
        computer_type = re.findall('[A-Z][^A-Z]*', computer_type)
        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with {' '.join(word.lower() for word in computer_type)} "
                             f"{self.manufacturer} {self.model}!")

        if ram > self.max_ram or not self.power_of_two(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with "
                             f"{' '.join(word.lower() for word in computer_type)} {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)

        return f"Created {self.__repr__()} for {self.price}$."

    def set_parts(self, processor: str, ram: int) -> None:
        self.processor = processor
        self.ram = ram
        self.price += self.available_processors[processor]
        self.price += int(log2(ram)) * 100

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
