from project.animal import Animal
from project.worker import Worker
from typing import List


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            self.__workers_capacity += 1
        except IndexError:
            return f"There is no {worker_name} in the zoo"

        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        money_to_pay = sum(w.salary for w in self.workers)

        if money_to_pay <= self.__budget:
            self.__budget -= money_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        money_to_feed_animals = sum(a.money_for_care for a in self.animals)

        if money_to_feed_animals <= self.__budget:
            self.__budget -= money_to_feed_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def get_different_entities_status(self, entity: str, type: str) -> str:
        if type == "animals":
            entities = [e for e in self.animals if e.__class__.__name__ == entity]
        else:
            entities = [e for e in self.workers if e.__class__.__name__ == entity]
        amount_of_entities = len(entities)
        final_string = f"----- {amount_of_entities} {entity}s:\n"
        for current_entity in entities:
            final_string += f"{current_entity}\n"

        return final_string

    def animals_status(self):
        type = "animals"
        result = f"You have {len(self.animals)} animals\n"
        result += self.get_different_entities_status("Lion", type)
        result += self.get_different_entities_status("Tiger", type)
        result += self.get_different_entities_status("Cheetah", type)

        return result.strip()

    def workers_status(self):
        type = "workers"
        result = f"You have {len(self.workers)} workers\n"
        result += self.get_different_entities_status("Keeper", type)
        result += self.get_different_entities_status("Caretaker", type)
        result += self.get_different_entities_status("Vet", type)

        return result.strip()
