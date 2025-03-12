import sys  # Import system module for exiting the program
from models import session, Team, Player, Tournament, Match  # Import database models and session


def add_team():
    #team
    """Add a new team to the database."""
    name = input("Enter team name: ")
    if session.query(Team).filter_by(name=name).first():
        print("Team already exists!")
        return
    team = Team(name=name)
    session.add(team)
    session.commit()
    print(f"Team '{name}' added successfully!")


def add_player():
    #players
    """Add a new player to the database."""
    name = input("Enter player's name: ")
    game = input("Enter game: ")
    team_id = input("Enter team ID (or leave blank for no team): ")
    
    player = Player(name=name, game=game, team_id=int(team_id) if team_id else None)
    session.add(player)
    session.commit()
    print(f"Player '{name}' added successfully!")


def add_tournament():
    #tournamentS
    """Create a new tournament."""
    name = input("Enter tournament name: ")
    game = input("Enter game for the tournament: ")
    if session.query(Tournament).filter_by(name=name).first():
        print("Tournament already exists!")
        return
    tournament = Tournament(name=name, game=game)
    session.add(tournament)
    session.commit()
    print(f"Tournament '{name}' added successfully!")


def add_match():
    #matchS
    """Add a match between two players."""
    tournament_id = input("Enter tournament ID: ")
    player1_id = input("Enter Player 1 ID: ")
    player2_id = input("Enter Player 2 ID: ")
    
    match = Match(player1_id=int(player1_id), player2_id=int(player2_id), tournament_id=int(tournament_id))
    session.add(match)
    session.commit()
    print(f"Match between Player {player1_id} and Player {player2_id} added!")


def record_winner():
    #winner_records
    """Update a match with the winner."""
    match_id = input("Enter match ID: ")
    winner_id = input("Enter winning player ID: ")
    
    match = session.query(Match).get(int(match_id))
    if match:
        match.winner_id = int(winner_id)
        session.commit()
        print(f"Player {winner_id} is the winner of Match {match_id}!")
    else:
        print("Match not found!")


def list_teams():
    #creating list for teams
    """List all teams."""
    teams = session.query(Team).all()
    if not teams:
        print("No teams available.")
    else:
        for team in teams:
            print(f"[ID: {team.id}] {team.name}")


def list_players_by_team():
    #listing players by there teams
    """List all players in a specific team."""
    team_id = input("Enter team ID: ")
    players = session.query(Player).filter_by(team_id=int(team_id)).all()
    
    if not players:
        print(f"No players found in team {team_id}.")
    else:
        print(f"Players in Team {team_id}:")
        for player in players:
            print(f"[ID: {player.id}] {player.name} - {player.game}")


def list_tournaments():
    #list for tornaments
    """List all tournaments."""
    tournaments = session.query(Tournament).all()
    if not tournaments:
        print("No tournaments available.")
    else:
        for tournament in tournaments:
            print(f"[ID: {tournament.id}] {tournament.name} - Game: {tournament.game}")


def list_matches():
    #list for matches
    """List all matches."""
    matches = session.query(Match).all()
    if not matches:
        print("No matches found.")
    else:
        for match in matches:
            print(f"[ID: {match.id}] Player {match.player1_id} vs Player {match.player2_id} - Winner: {match.winner_id or 'TBD'} (Tournament ID: {match.tournament_id})")


def main():
    #cli interactive for users
    """Main CLI menu for eSports Tournament management."""
    #looping throught .
    while True:
        print("\n🎮 eSports Tournament 🎮")
        print("🏆️The Future Of Gaming 🏅️")
        print("1. 👫️Add Team👫️")
        print("2. 🤴️Add Player👸️")
        print("3. 🗡️ Add Tournament🀄️")
        print("4. ⚔️ Add Match🀄️")
        print("5. 🎮️Record Match Winner🏆️")
        print("6. ✴️List Teams✴️")
        print("7. ✴️List Players by Team✴️")
        print("8. 📜️List Tournaments📜️")
        print("9. 📃️List Matches📃️")
        print("10. Exit⛩️")

        choice = input("\nEnter choice here: ")
        if choice == "1":
            add_team()
        elif choice == "2":
            add_player()
        elif choice == "3":
            add_tournament()
        elif choice == "4":
            add_match()
        elif choice == "5":
            record_winner()
        elif choice == "6":
            list_teams()
        elif choice == "7":
            list_players_by_team()
        elif choice == "8":
            list_tournaments()
        elif choice == "9":
            list_matches()
        elif choice == "10":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()  # Start the CLI program
