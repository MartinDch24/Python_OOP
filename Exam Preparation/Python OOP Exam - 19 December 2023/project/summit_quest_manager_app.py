from project.peaks.summit_peak import SummitPeak
from project.peaks.arctic_peak import ArcticPeak
from project.climbers.summit_climber import SummitClimber
from project.climbers.arctic_climber import ArcticClimber


class SummitQuestManagerApp:
    CLIMBERS = {"SummitClimber": SummitClimber, "ArcticClimber": ArcticClimber}
    PEAKS = {"SummitPeak": SummitPeak, "ArcticPeak": ArcticPeak}

    def __init__(self):
        self.climbers: SummitClimber or ArcticClimber = []
        self.peaks: SummitPeak or ArcticPeak = []
        self.conquered_peaks = set()

    def register_climber(self, climber_type: str, climber_name: str) -> str:
        if climber_type not in SummitQuestManagerApp.CLIMBERS:
            return f"{climber_type} doesn't exist in our register."

        try:
            next(filter(lambda c: c.name == climber_name, self.climbers))
            return f"{climber_name} has been already registered."
        except StopIteration:
            pass

        climber = SummitQuestManagerApp.CLIMBERS[climber_type](climber_name)
        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int) -> str:
        if peak_type not in SummitQuestManagerApp.PEAKS:
            return f"{peak_type} is an unknown type of peak."

        peak = SummitQuestManagerApp.PEAKS[peak_type](peak_name, peak_elevation)
        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: list) -> str:
        climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        peak = next(filter(lambda p: p.name == peak_name, self.peaks))

        recommended_gear = peak.get_recommended_gear()

        if gear == recommended_gear:
            return f"{climber_name} is prepared to climb {peak_name}."

        missing_gear = []

        for i in range(len(gear)):
            if gear[i] != recommended_gear[i]:
                missing_gear.append(gear[i])
        if len(recommended_gear) > len(gear):
            missing_gear.extend(g for g in recommended_gear[len(gear):])

        climber.is_prepared = False

        return (f"{climber_name} is not prepared to climb {peak_name}. "
                f"Missing gear: {', '.join(sorted(missing_gear))}.")

    def perform_climbing(self, climber_name: str, peak_name: str) -> str:
        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        elif not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        climber.climb(peak)
        self.conquered_peaks.add(peak.name)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self):
        result = f"Total climbed peaks: {len(self.conquered_peaks)}\n**Climber's statistics:**"

        self.climbers = [c for c in self.climbers if len(c.conquered_peaks) > 0]
        self.climbers = sorted(self.climbers, key=lambda c: (-len(c.conquered_peaks), c.name))

        for climber in self.climbers:
            climber.conquered_peaks = sorted(climber.conquered_peaks)
            result += f"\n{str(climber)}"

        return result
