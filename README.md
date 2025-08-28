# Arcade Hall Management System

A Python CLI app for managing an Arcade Hall where players can register, play games, and track high scores.

## Features

- Player registration with unique usernames
- Score recording for different games
- Leaderboard viewing for each game

## Usage

### Register a player
```bash
python cli.py register <username>
```

### Record a score
```bash
python cli.py score <username> <game_name> <score>
```

### View leaderboard
```bash
python cli.py leaderboard <game_name>
```

## Examples

```bash
# Register players
python cli.py register alice
python cli.py register bob

# Record scores
python cli.py score alice "Pac-Man" 15000
python cli.py score bob "Pac-Man" 12000
python cli.py score alice "Street Fighter" 8500

# View leaderboards
python cli.py leaderboard "Pac-Man"
python cli.py leaderboard "Street Fighter"
```