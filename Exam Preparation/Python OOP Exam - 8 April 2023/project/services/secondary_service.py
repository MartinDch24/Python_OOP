from project.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name: str):
        super().__init__(name, 15)

    def add_robot(self, robot):
        if robot.__class__.__name__ != "FemaleRobot":
            return False

        self.robots.append(robot)
        return True

    def details(self):
        return f"{self.name} Secondary Service:\nRobots: {' '.join(r.name for r in self.robots) if self.robots else 'none'}"
