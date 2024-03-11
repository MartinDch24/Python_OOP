from typing import List

from project.animals.animal import Bird
from project.food import Food, Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    @property
    def food_that_eats(self) -> List[Food]:
        return [Meat]

    def make_sound(self) -> str:
        return "Hoot Hoot"

    @property
    def gained_weight(self) -> float:
        return 0.25


class Hen(Bird):
    @property
    def food_that_eats(self) -> List[Food]:
        return [Meat, Fruit, Vegetable, Seed]

    def make_sound(self) -> str:
        return "Cluck"

    @property
    def gained_weight(self) -> float:
        return 0.35
