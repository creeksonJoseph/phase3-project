import click
from lib.db.models import Player, Score, Game, Base, engine
from lib.db.seed import seed_data

class ArcadeHallCLI:
    def __init__(self):
        Base.metadata.create_all(engine)
    
    def register_player(self):
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty!")
            return
        
        player_id = Player.create(username)
        if player_id:
            print(f"Player '{username}' registered successfully!")
        else:
            print(f"Username '{username}' already exists!")
    
    def record_score(self):
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty!")
            return
        
        player = Player.find_by_username(username)
        if not player:
            print(f"Player '{username}' not found! Please register first.")
            return
            
        game_name = input("Enter game name: ").strip()
        if not game_name:
            print("Game name cannot be empty!")
            return
            
        try:
            score = int(input("Enter score: "))
        except ValueError:
            print("Score must be a number!")
            return
        
        Score.create(player.id, game_name, score)
        print(f"Score {score} recorded for {username} in {game_name}!")
    
    def view_leaderboard(self):
        game_name = input("Enter game name: ").strip()
        if not game_name:
            print("Game name cannot be empty!")
            return
            
        scores = Score.get_leaderboard(game_name)
        if not scores:
            print(f"No scores found for game '{game_name}'")
            return
        
        print(f"\n=== {game_name} Leaderboard ===")
        for i, (username, score) in enumerate(scores, 1):
            print(f"{i}. {username}: {score}")
    
    def view_all_players(self):
        players = Player.get_all()
        if not players:
            print("No players registered yet!")
            return
        
        print("\n=== All Players ===")
        for player in players:
            print(f"- {player.username}")
    
    def view_all_games(self):
        games = Game.get_all()
        if not games:
            print("No games available!")
            return
        
        print("\n=== Available Games ===")
        for game in games:
            print(f"- {game.name} ({game.category})")
    
    def delete_player(self):
        username = input("Enter username to delete: ").strip()
        if not username:
            print("Username cannot be empty!")
            return
        
        player = Player.find_by_username(username)
        if not player:
            print(f"Player '{username}' not found!")
            return
        
        confirm = input(f"Are you sure you want to delete '{username}'? (y/N): ").strip().lower()
        if confirm == 'y':
            player.delete()
            print(f"Player '{username}' deleted successfully!")
        else:
            print("Deletion cancelled.")
    
    def seed_database(self):
        seed_data()

def show_menu():
    menu_options = {
        "1": "Register a new player",
        "2": "Record a score", 
        "3": "View leaderboard",
        "4": "View all players",
        "5": "View all games",
        "6": "Delete a player",
        "7": "Seed sample data",
        "0": "Exit"
    }
    
    print("\n" + "="*50)
    print("🎮 ARCADE HALL MANAGEMENT SYSTEM 🎮")
    print("="*50)
    print("Please select an option:")
    
    for key, value in menu_options.items():
        print(f"{key}. {value}")
    
    print("="*50)
    return menu_options

def run_cli():
    cli = ArcadeHallCLI()
    
    print("\n🎮 Welcome to Arcade Hall Management System! 🎮")
    
    while True:
        menu_options = show_menu()
        choice = input("> ").strip()
        
        if choice == "0":
            print("\nThanks for using Arcade Hall Management System!")
            print("Goodbye! 🎮")
            break
        elif choice == "1":
            cli.register_player()
        elif choice == "2":
            cli.record_score()
        elif choice == "3":
            cli.view_leaderboard()
        elif choice == "4":
            cli.view_all_players()
        elif choice == "5":
            cli.view_all_games()
        elif choice == "6":
            cli.delete_player()
        elif choice == "7":
            cli.seed_database()
        else:
            print(f"Invalid choice! Please select a number from 0-7.")