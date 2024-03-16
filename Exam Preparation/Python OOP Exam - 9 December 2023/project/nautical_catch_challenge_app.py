from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    DIVER_TYPES = {'ScubaDiver': ScubaDiver, 'FreeDiver': FreeDiver}
    FISH_TYPES = {'DeepSeaFish': DeepSeaFish, 'PredatoryFish': PredatoryFish}

    def __init__(self):
        self.divers: ScubaDiver or FreeDiver = []
        self.fish_list: DeepSeaFish or PredatoryFish = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        try:
            next(filter(lambda d: d.name == diver_name, self.divers))
            return f"{diver_name} is already a participant."
        except StopIteration:
            pass

        new_diver = self.DIVER_TYPES[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            next(filter(lambda f: f.name == fish_name, self.fish_list))
            return f"{fish_name} is already permitted."
        except StopIteration:
            pass

        new_fish = self.FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                diver.update_health_status()
                return f"{diver_name} hits a {fish.points:.1f}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points:.1f}pt. {fish_name}."

    def health_recovery(self):
        divers_in_need_of_recovery = [d for d in self.divers if d.has_health_issue]
        for current_diver in divers_in_need_of_recovery:
            current_diver.update_health_status()
            current_diver.renew_oxy()

        return f"Divers recovered: {len(divers_in_need_of_recovery)}"

    def diver_catch_report(self, diver_name: str):
        diver = next(filter(lambda d: d.name == diver_name, self.divers))

        result = f'**{diver_name} Catch Report**'
        for fish in diver.catch:
            result += f'\n{fish.fish_details()}'

        return result

    def competition_statistics(self):
        self.divers = sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        result = '**Nautical Catch Challenge Statistics**'
        for diver in self.divers:
            result += f'\n{str(diver)}'

        return result
