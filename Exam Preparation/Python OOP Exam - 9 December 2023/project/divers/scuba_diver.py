from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    MAX_OXYGEN = 540

    def __init__(self, name):
        super().__init__(name, ScubaDiver.MAX_OXYGEN)

    def miss(self, time_to_catch: int):
        if self.oxygen_level >= round(0.3 * time_to_catch):
            self.oxygen_level -= round(0.3 * time_to_catch)
        else:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.MAX_OXYGEN
