from lib.db.database import Database

def seed_data():
    """Populate database with sample data for testing"""
    db = Database()
    
    # Sample players
    players = ["alice", "bob", "charlie", "diana", "eve"]
    
    # Sample games and scores
    sample_data = [
        ("alice", "Pac-Man", 15000),
        ("bob", "Pac-Man", 12000),
        ("charlie", "Pac-Man", 18000),
        ("alice", "Street Fighter", 8500),
        ("bob", "Street Fighter", 9200),
        ("diana", "Street Fighter", 7800),
        ("eve", "Galaga", 22000),
        ("charlie", "Galaga", 19500),
        ("alice", "Donkey Kong", 14000),
        ("bob", "Donkey Kong", 16500),
    ]
    
    # Register players
    for player in players:
        db.register_player(player)
        print(f"Registered player: {player}")
    
    # Add scores
    for username, game, score in sample_data:
        db.record_score(username, game, score)
        print(f"Added score: {username} - {game}: {score}")
    
    print("\nSample data seeded successfully!")

if __name__ == "__main__":
    seed_data()