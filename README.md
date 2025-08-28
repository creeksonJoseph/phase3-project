# Arcade Hall Management System

A Python CLI application for managing an Arcade Hall where players can register, play games, and track high scores. This system provides a complete solution for arcade operators to manage player registrations, record game scores, and display leaderboards.

## 🎮 Features

- **Player Registration**: Register new players with unique usernames
- **Score Recording**: Record scores for different arcade games
- **Leaderboard System**: View top 10 high scores for each game
- **Database Persistence**: SQLAlchemy ORM with SQLite database
- **Sample Data Seeding**: Populate database with test data using Faker
- **CRUD Operations**: Create, read, update, delete for all entities
- **Database Migrations**: Alembic for schema management

## 🏗️ Project Structure

```
project/
├── lib/                           # Main application library
│   ├── __init__.py               # Package initialization
│   ├── cli.py                    # Interactive CLI interface
│   └── db/                       # Database module
│       ├── __init__.py           # Database package initialization
│       ├── models.py             # SQLAlchemy ORM models
│       ├── seed.py               # Sample data seeding with Faker
│       └── migrations/           # Alembic migration files
│           ├── env.py            # Migration environment
│           └── versions/         # Migration versions
├── cli.py                        # Main entry point
├── Pipfile                       # Pipenv dependencies
├── Pipfile.lock                  # Locked dependency versions
├── alembic.ini                   # Alembic configuration
└── README.md                     # Project documentation
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

### Starting the Application

```bash
python cli.py
```

This will start the interactive menu system where you can perform all operations without retyping the command.

### Interactive Menu Options

Once you start the application, you'll see a menu with the following options:

```
🎮 ARCADE HALL MANAGEMENT SYSTEM 🎮
Please select an option:
1. Register a new player
2. Record a score
3. View leaderboard
4. Seed sample data
0. Exit
```

#### Option 1: Register a New Player
- Select option `1`
- Enter a unique username when prompted
- System will confirm successful registration or notify if username exists

#### Option 2: Record a Score
- Select option `2`
- Enter the player's username
- Enter the game name
- Enter the score (must be a number)
- System will record the score or notify if player doesn't exist

#### Option 3: View Leaderboard
- Select option `3`
- Enter the game name
- System displays top 10 scores for that game

#### Option 4: Seed Sample Data
- Select option `4`
- System populates database with sample players and scores
- Useful for testing and demonstration

#### Option 0: Exit
- Select option `0` to exit the application

### Example Session

```
🎮 Welcome to Arcade Hall Management System! 🎮

> 4  (Seed sample data)
Sample data added successfully!

> 1  (Register new player)
Enter username: john
Player 'john' registered successfully!

> 2  (Record score)
Enter username: john
Enter game name: Pac-Man
Enter score: 20000
Score 20000 recorded for john in Pac-Man!

> 3  (View leaderboard)
Enter game name: Pac-Man
=== Pac-Man Leaderboard ===
1. john: 20000
2. charlie: 18000
3. alice: 15000

> 0  (Exit)
Thanks for using Arcade Hall Management System!
Goodbye! 🎮
```

## 🗄️ Database Schema

The application uses SQLite with the following schema:

### Players Table

| Column   | Type    | Description        |
| -------- | ------- | ------------------ |
| id       | INTEGER | Primary key        |
| username | TEXT    | Unique player name |

### Scores Table

| Column    | Type    | Description            |
| --------- | ------- | ---------------------- |
| id        | INTEGER | Primary key            |
| player_id | INTEGER | Foreign key to players |
| game_name | TEXT    | Name of the game       |
| score     | INTEGER | Score achieved         |

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

- **Interactive CLI**: Menu-driven interface that keeps users engaged
- **Input Validation**: Validates all user inputs with helpful error messages
- **Modular Design**: Separated concerns with clear module boundaries
- **Database Layer**: Isolated database operations in `lib/db/`
- **CLI Layer**: Interactive interface logic in `lib/cli.py`
- **Data Models**: Type-safe data structures in `models.py`

### Testing with Sample Data

Use menu option 4 to quickly populate the database with sample data.

This creates:
- 5 sample players (alice, bob, charlie, diana, eve)
- 10 sample scores across 4 different games (Pac-Man, Street Fighter, Galaga, Donkey Kong)
- Realistic test data for development and demonstration

## 🔧 Technical Details

### Dependencies

- **SQLAlchemy**: ORM for database operations and relationships
- **Alembic**: Database migration management
- **Click**: Enhanced CLI framework (imported but not fully utilized)
- **Faker**: Realistic test data generation
- **SQLite3**: Built-in database support
- **Typing**: Type hints for better code quality

### Error Handling

- **Input Validation**: Validates empty inputs and invalid data types
- **Duplicate Username Prevention**: Graceful handling of registration conflicts
- **Player Validation**: Clear error messages for unregistered players
- **Database Error Management**: Proper exception handling for database operations
- **Menu Validation**: Handles invalid menu choices with helpful messages

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
