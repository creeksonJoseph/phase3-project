import sqlite3
from typing import List, Tuple

class Database:
    def __init__(self, db_path: str = "arcade_hall.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS players (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS scores (
                    id INTEGER PRIMARY KEY,
                    player_id INTEGER,
                    game_name TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    FOREIGN KEY (player_id) REFERENCES players (id)
                )
            ''')
    
    def register_player(self, username: str) -> bool:
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("INSERT INTO players (username) VALUES (?)", (username,))
                return True
        except sqlite3.IntegrityError:
            return False
    
    def record_score(self, username: str, game_name: str, score: int) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT id FROM players WHERE username = ?", (username,))
            player = cursor.fetchone()
            if not player:
                return False
            conn.execute("INSERT INTO scores (player_id, game_name, score) VALUES (?, ?, ?)", 
                        (player[0], game_name, score))
            return True
    
    def get_leaderboard(self, game_name: str) -> List[Tuple[str, int]]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT p.username, MAX(s.score) as high_score
                FROM scores s
                JOIN players p ON s.player_id = p.id
                WHERE s.game_name = ?
                GROUP BY p.username
                ORDER BY high_score DESC
                LIMIT 10
            ''', (game_name,))
            return cursor.fetchall()