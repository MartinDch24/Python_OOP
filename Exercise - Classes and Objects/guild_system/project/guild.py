from project.player import Player
from typing import List


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:

        try:
            player_to_kick = next(filter(lambda p: p.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        player_to_kick.guild = "Unaffiliated"
        self.players.remove(player_to_kick)

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self) -> str:
        player_info = '\n'.join(p.player_info() for p in self.players)
        return f"Guild: {self.name}\n" \
               f"{player_info}"
