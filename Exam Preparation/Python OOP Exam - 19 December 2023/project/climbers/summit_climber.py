from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):

    def __init__(self, name):
        super().__init__(name, 150)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Advanced":
            multiplier = 1.3
        else:
            multiplier = 2.5

        self.strength -= 30 * multiplier

        self.conquered_peaks.append(peak.name)
