class Robot:

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 1


class MedicalRobot(Robot):

    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):

    @staticmethod
    def sensors_amount():
        return 12


class WarRobot(Robot):

    @staticmethod
    def sensors_amount():
        return 12


def number_of_robot_sensors(robot):
    print(robot.sensors_amount())
