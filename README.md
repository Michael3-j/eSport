## eSport management system
This project is a Command-Line Interface (CLI) application for managing eSports tournaments. Users can register players, create teams, set up tournaments, record match results, and list participants.

## Player & Team Management

1]Players can register with their name and game.

2]Players can join teams.

3]List all players in a specific team.

## Tournament System

1]Players register for a tournament.

2]Matchups are generated.

3]Winners are updated per round.


## Database Schema

# Tables:

1]Player (id, name, game, team_id)

2]Team (id, name)

3]Tournament (id, name, game)

4]Match (id, player1_id, player2_id, winner_id, tournament_id)

# Relationships:

One-to-Many: A team can have multiple players.

Many-to-One: A match belongs to a tournament


## Running the CLI

Just run pthon cli.py to be able to use the user interactive cli wich 
looks like this;
=>emojis are to make it more user friendly


🎮 eSports Tournament 🎮
🏆️The Future Of Gaming 🏅️
1. 👫️Add Team👫️
2. 🤴️Add Player👸️
3. 🗡️ Add Tournament🀄️
4. ⚔️Add Match🀄️
5. 🎮️Record Match Winner🏆️
6. ✴️List Teams✴️
7. ✴️List Players by Team✴️
8. 📜️List Tournaments📜️
9. 📃️List Matches📃️
10. Exit⛩️

Enter choice: 
