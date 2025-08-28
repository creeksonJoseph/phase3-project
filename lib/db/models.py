from dataclasses import dataclass

@dataclass
class Player:
    id: int
    username: str

@dataclass
class Score:
    id: int
    player_id: int
    game_name: str
    score: int