from faker import Faker
from lib.db.models import Player, Score, Game, Base, engine
import random

fake = Faker()

def seed_data():
    """Populate database with sample data using Faker"""
    # Create tables
    Base.metadata.create_all(engine)
    
    # Sample games data
    games_data = [
        ("Pac-Man", "Arcade"),
        ("Street Fighter", "Fighting"),
        ("Galaga", "Shooter"),
        ("Donkey Kong", "Platform"),
        ("Tetris", "Puzzle")
    ]
    
    # Create games (or use existing ones)
    game_names = []
    for name, category in games_data:
        game_id = Game.create(name, category)
        game_names.append(name)  # Add name regardless of creation success
        if game_id:
            print(f"Created game: {name}")
        else:
            print(f"Game already exists: {name}")
    
    # Create players with simple names to avoid duplicates
    player_names = ["alice", "bob", "charlie", "diana", "eve", "frank", "grace", "henry"]
    player_data = []
    for username in player_names:
        player_id = Player.create(username)
        if player_id:
            player_data.append((player_id, username))
            print(f"Created player: {username}")
        else:
            # Try to find existing player
            existing_player = Player.find_by_username(username)
            if existing_player:
                player_data.append((existing_player.id, username))
                print(f"Using existing player: {username}")
    
    # Create scores
    for player_id, username in player_data:
        # Each player gets 2-3 random scores
        num_scores = random.randint(2, 3)
        for _ in range(num_scores):
            game_name = random.choice(game_names)
            score = random.randint(1000, 50000)
            Score.create(player_id, game_name, score)
            print(f"Added score: {username} - {game_name}: {score}")
    
    print("\nSample data seeded successfully!")

if __name__ == "__main__":
    seed_data()