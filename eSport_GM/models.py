from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine

Base = declarative_base()
# 4 classes and tables.
class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False, unique=True)

# One-to-Many: A team can have multiple players
    players = relationship("Player", back_populates="team")


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    game = Column(String(), nullable=False)
    team_id = Column(Integer(), ForeignKey("teams.id"))

# Many-to-One: A player belongs to one team
    team = relationship("Team", back_populates="players")


class Tournament(Base):

    __tablename__ = "tournaments"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False, unique=True)
    game = Column(String(), nullable=False)

# One-to-Many: A tournament can have multiple matches
    matches = relationship("Match", back_populates="tournament")

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer(), primary_key=True)
    player1_id = Column(Integer(), ForeignKey("players.id"), nullable=False)
    player2_id = Column(Integer(), ForeignKey("players.id"), nullable=False)
    winner_id = Column(Integer(), ForeignKey("players.id"), nullable=True)
    tournament_id = Column(Integer(), ForeignKey("tournaments.id"), nullable=False)


    # Many-to-One: A match belongs to one tournament
    tournament = relationship("Tournament", back_populates="matches")
    # Many-to-One: Each match has two players
    player1 = relationship("Player", foreign_keys=[player1_id])
    player2 = relationship("Player", foreign_keys=[player2_id])

    # Many-to-One: The winner is a player
    winner = relationship("Player", foreign_keys=[winner_id])


# Create the SQLite database
engine = create_engine("sqlite:///eSport.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()