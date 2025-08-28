import argparse
from database import Database

class ArcadeHallCLI:
    def __init__(self):
        self.db = Database()
    
    def register(self, username: str):
        if self.db.register_player(username):
            print(f"Player '{username}' registered successfully!")
        else:
            print(f"Username '{username}' already exists!")
    
    def record_score(self, username: str, game: str, score: int):
        if self.db.record_score(username, game, score):
            print(f"Score {score} recorded for {username} in {game}!")
        else:
            print(f"Player '{username}' not found! Please register first.")
    
    def leaderboard(self, game: str):
        scores = self.db.get_leaderboard(game)
        if not scores:
            print(f"No scores found for game '{game}'")
            return
        
        print(f"\n=== {game} Leaderboard ===")
        for i, (username, score) in enumerate(scores, 1):
            print(f"{i}. {username}: {score}")

def main():
    cli = ArcadeHallCLI()
    parser = argparse.ArgumentParser(description="Arcade Hall Management System")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Register command
    register_parser = subparsers.add_parser('register', help='Register a new player')
    register_parser.add_argument('username', help='Player username')
    
    # Score command
    score_parser = subparsers.add_parser('score', help='Record a score')
    score_parser.add_argument('username', help='Player username')
    score_parser.add_argument('game', help='Game name')
    score_parser.add_argument('score', type=int, help='Score achieved')
    
    # Leaderboard command
    leaderboard_parser = subparsers.add_parser('leaderboard', help='View game leaderboard')
    leaderboard_parser.add_argument('game', help='Game name')
    
    args = parser.parse_args()
    
    if args.command == 'register':
        cli.register(args.username)
    elif args.command == 'score':
        cli.record_score(args.username, args.game, args.score)
    elif args.command == 'leaderboard':
        cli.leaderboard(args.game)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()