# Functionalities 
from models import session, Player, Team, Tournament, Match # Import database models and session

# Function to add a new team
def add_team(name):
    # Check if the team already exists using session.query().filter_by().first
    existing_team = session.query(Team).filter_by(name=name).first()
    if existing_team:
        print(f"Team '{name}' already exists!! Choose a different name.")
        return
    
    # If the team does not exist, add it
    team = Team(name=name)
    session.add(team)
    session.commit()
    print(f"Team '{name}' has been added successfully🥳!")


# Function to add a player and assign them to a team
def add_player(name, game, team_name):
    team = session.query(Team).filter_by(name=team_name).first()
    if not team:
        print("Team not found!! Add the team first.")
        return
    player = Player(name=name, game=game, team=team)
    session.add(player)
    session.commit()

# Function to list all players in a specific team
def list_team_players(team_name):
    team = session.query(Team).filter_by(name=team_name).first()
    if not team:
        print("Team not found!!")
        return
    print(f"Players in {team.name}:")
    for player in team.players:
        print(f"- {player.name} ({player.game})")

# Function to create a new tournament
def create_tournament(name, game):
    tournament = Tournament(name=name, game=game)
    session.add(tournament)
    session.commit()

# Function to add a match between two players in a tournament
def add_match(player1_name, player2_name, tournament_name):
    player1 = session.query(Player).filter_by(name=player1_name).first()
    player2 = session.query(Player).filter_by(name=player2_name).first()
    tournament = session.query(Tournament).filter_by(name=tournament_name).first()

    if not all([player1, player2, tournament]):
        print("Player or Tournament not found!!")
        return

    match = Match(player1=player1, player2=player2, tournament=tournament)
    session.add(match)
    session.commit()

# Function to update the winner of a match
def update_match_winner(match_id, winner_name):
    match = session.query(Match).filter_by(id=match_id).first()
    winner = session.query(Player).filter_by(name=winner_name).first()

    if not match or not winner:
        print("Match or winner not found!!")
        return

    match.winner = winner
    session.commit()

# Sample Data (For Testing)
add_team("Team KETA4")
add_team("Team WTF")

add_player("KETA4**Alice", "PUBG_MOBILE", "Team KETA4")
add_player("KETA4**Bob", "PUBG_MOBILE", "Team KETA4")
add_player("WTF^#Charlie", "PUBG_MOBILE", "Team WTF")

list_team_players("Team KETA4")

create_tournament("Spring Tournament", "Valorant")

add_match("KETA4**Alice", "WTF^#Charlie", "Spring Tournament")
update_match_winner(1, "KETA4**Alice")  # Update match with winner
