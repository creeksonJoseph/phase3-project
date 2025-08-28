# Arcade Hall Management System

A Python CLI application for managing an Arcade Hall where players can register, play games, and track high scores. This system provides a complete solution for arcade operators to manage player registrations, record game scores, and display leaderboards.

## 🎮 Features

- **Player Registration**: Register new players with unique usernames
- **Score Recording**: Record scores for different arcade games
- **Leaderboard System**: View top 10 high scores for each game
- **Database Persistence**: SQLite database for reliable data storage
- **Sample Data Seeding**: Populate database with test data for development

## 🏗️ Project Structure

```
project/
├── lib/                    # Main application library
│   ├── __init__.py        # Package initialization
│   ├── cli.py             # Command-line interface logic
│   └── db/                # Database module
│       ├── __init__.py    # Database package initialization
│       ├── database.py    # Database operations and queries
│       ├── models.py      # Data models (Player, Score)
│       └── seed.py        # Sample data seeding
├── cli.py                 # Main entry point
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only standard library)

### Setup
1. Clone or download the project
2. Navigate to the project directory
3. The application is ready to run (no pip install needed)

## 📖 Usage

### Available Commands

#### Register a Player
```bash
python cli.py register <username>
```
Register a new player with a unique username.

**Example:**
```bash
python cli.py register alice
# Output: Player 'alice' registered successfully!
```

#### Record a Score
```bash
python cli.py score <username> <game_name> <score>
```
Record a score for an existing player in a specific game.

**Example:**
```bash
python cli.py score alice "Pac-Man" 15000
# Output: Score 15000 recorded for alice in Pac-Man!
```

#### View Leaderboard
```bash
python cli.py leaderboard <game_name>
```
Display the top 10 high scores for a specific game.

**Example:**
```bash
python cli.py leaderboard "Pac-Man"
# Output:
# === Pac-Man Leaderboard ===
# 1. charlie: 18000
# 2. alice: 15000
# 3. bob: 12000
```

#### Seed Sample Data
```bash
python cli.py seed
```
Populate the database with sample players and scores for testing.

### Complete Example Workflow

```bash
# 1. Seed the database with sample data
python cli.py seed

# 2. Register additional players
python cli.py register john
python cli.py register sarah

# 3. Record some scores
python cli.py score john "Pac-Man" 20000
python cli.py score sarah "Street Fighter" 9500
python cli.py score john "Galaga" 25000

# 4. View leaderboards
python cli.py leaderboard "Pac-Man"
python cli.py leaderboard "Street Fighter"
python cli.py leaderboard "Galaga"

# 5. Get help
python cli.py --help
```

## 🗄️ Database Schema

The application uses SQLite with the following schema:

### Players Table
| Column   | Type    | Description           |
|----------|---------|----------------------|
| id       | INTEGER | Primary key          |
| username | TEXT    | Unique player name   |

### Scores Table
| Column    | Type    | Description              |
|-----------|---------|--------------------------|
| id        | INTEGER | Primary key              |
| player_id | INTEGER | Foreign key to players   |
| game_name | TEXT    | Name of the game         |
| score     | INTEGER | Score achieved           |

## 🎯 Key Features Explained

### Player Management
- **Unique Usernames**: Each player must have a unique username
- **Simple Registration**: One-command player registration
- **Automatic Validation**: System prevents duplicate usernames

### Score Tracking
- **Multi-Game Support**: Track scores across different arcade games
- **Player Validation**: Only registered players can record scores
- **Unlimited Entries**: Players can have multiple scores per game

### Leaderboard System
- **Top 10 Display**: Shows the highest 10 scores per game
- **Best Score Only**: Displays each player's highest score per game
- **Sorted Rankings**: Automatically sorted from highest to lowest

### Data Persistence
- **SQLite Database**: Reliable local database storage
- **Automatic Setup**: Database and tables created automatically
- **Data Integrity**: Foreign key constraints ensure data consistency

## 🛠️ Development

### Code Organization
- **Modular Design**: Separated concerns with clear module boundaries
- **Database Layer**: Isolated database operations in `lib/db/`
- **CLI Layer**: Command-line interface logic in `lib/cli.py`
- **Data Models**: Type-safe data structures in `models.py`

### Testing with Sample Data
Use the seed command to quickly populate the database:
```bash
python cli.py seed
```

This creates:
- 5 sample players (alice, bob, charlie, diana, eve)
- 10 sample scores across 4 different games
- Realistic test data for development and demonstration

## 🔧 Technical Details

### Dependencies
- **Python Standard Library Only**: No external packages required
- **SQLite3**: Built-in database support
- **Argparse**: Command-line argument parsing
- **Typing**: Type hints for better code quality
- **Dataclasses**: Clean data model definitions

### Error Handling
- **Duplicate Username Prevention**: Graceful handling of registration conflicts
- **Player Validation**: Clear error messages for unregistered players
- **Database Error Management**: Proper exception handling for database operations

### Performance Considerations
- **Efficient Queries**: Optimized SQL queries with proper indexing
- **Connection Management**: Proper database connection handling
- **Memory Usage**: Minimal memory footprint with standard library usage

## 📝 License

This project is created for educational purposes as part of a Phase 3 CLI project template.

## 🤝 Contributing

This is an educational project. Feel free to fork and modify for learning purposes.

---

**Happy Gaming! 🎮**