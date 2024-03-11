from typing import List

from project.animals.animal import Mammal
from project.food import Food, Meat, Vegetable, Fruit, Seed


class Mouse(Mammal):
    @property
    def food_that_eats(self) -> List[Food]:
        return [Fruit, Vegetable]

    def make_sound(self) -> str:
        return "Squeak"

    @property
    def gained_weight(self) -> float:
        return 0.10


class Dog(Mammal):
    @property
    def food_that_eats(self) -> List[Food]:
        return [Meat]

    def make_sound(self) -> str:
        return "Woof!"

    @property
    def gained_weight(self) -> float:
        return 0.40


class Cat(Mammal):
    @property
    def food_that_eats(self) -> List[Food]:
        return [Meat, Vegetable]

    def make_sound(self) -> str:
        return "Meow"

    @property
    def gained_weight(self) -> float:
        return 0.30


class Tiger(Mammal):
    @property
    def food_that_eats(self) -> List[Food]:
        return [Meat]

    def make_sound(self) -> str:
        return "ROAR!!!"

    @property
    def gained_weight(self) -> float:
        return 1
