from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    VALID_ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}
    VALID_SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        try:
            new_service = self.VALID_SERVICE_TYPES[service_type](name)
        except KeyError:
            raise Exception("Invalid service type!")

        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        try:
            new_robot = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        except KeyError:
            raise Exception("Invalid robot type!")

        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(filter(lambda r: r.name == robot_name, self.robots))
        service = next(filter(lambda s: s.name == service_name, self.services))

        can_add_robot = service.add_robot(robot)
        if not can_add_robot:
            return "Unsuitable service."

        if len(service.robots) > service.capacity:
            service.robots.pop()
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))

        try:
            robot = next(filter(lambda r: r.name == robot_name, service.robots))
        except StopIteration:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))

        if service.robots:
            for robot in service.robots:
                robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        total_price = 0
        service = next(filter(lambda s: s.name == service_name, self.services))

        if service.robots:
            for robot in service.robots:
                total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = ""
        for service in self.services:
            result += f"{service.details()}\n"

        return result.rstrip()

