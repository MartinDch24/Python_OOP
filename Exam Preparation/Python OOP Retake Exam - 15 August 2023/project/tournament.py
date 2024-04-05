from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam
from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad


class Tournament:
    VALID_EQUIPMENT = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAMS = {"IndoorTeam": IndoorTeam, "OutdoorTeam": OutdoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        try:
            new_equipment = self.VALID_EQUIPMENT[equipment_type]()
        except KeyError:
            raise Exception("Invalid equipment type!")

        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        try:
            new_team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        except KeyError:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = next(filter(lambda e: e.__class__.__name__ == equipment_type, self.equipment[::-1]))
        team = next(filter(lambda t: t.name == team_name, self.teams))

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        altered_equipment = 0

        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                e.increase_price()
                altered_equipment += 1

        return f"Successfully changed {altered_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        first_team = next(filter(lambda t: t.name == team_name1, self.teams))
        second_team = next(filter(lambda t: t.name == team_name2, self.teams))

        if first_team.__class__.__name__ != second_team.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        first_sum = first_team.get_total_protection() + first_team.advantage
        second_sum = second_team.get_total_protection() + second_team.advantage

        if first_sum > second_sum:
            first_team.win()
            return f"The winner is {first_team.name}."
        elif first_sum < second_sum:
            second_team.win()
            return f"The winner is {second_team.name}."
        return "No winner in this game."

    def get_statistics(self):
        self.teams = sorted(self.teams, key=lambda t: -t.wins)
        joined_team_statistics = '\n'.join(t.get_statistics() for t in self.teams)
        return (f"Tournament: {self.name}\n"
                f"Number of Teams: {len(self.teams)}\n"
                f"Teams:\n"
                f"{joined_team_statistics}")
