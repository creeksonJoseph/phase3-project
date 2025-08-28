from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///arcade_hall.db')
Session = sessionmaker(bind=engine)

class Player(Base):
    __tablename__ = 'players'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    
    scores = relationship("Score", back_populates="player", cascade="all, delete-orphan")
    
    @classmethod
    def create(cls, username):
        session = Session()
        try:
            player = cls(username=username)
            session.add(player)
            session.commit()
            player_id = player.id
            return player_id
        except Exception:
            session.rollback()
            return None
        finally:
            session.close()
    
    @classmethod
    def find_by_username(cls, username):
        session = Session()
        try:
            return session.query(cls).filter_by(username=username).first()
        finally:
            session.close()
    
    @classmethod
    def get_all(cls):
        session = Session()
        try:
            return session.query(cls).all()
        finally:
            session.close()
    
    def delete(self):
        session = Session()
        try:
            session.delete(self)
            session.commit()
        finally:
            session.close()

class Score(Base):
    __tablename__ = 'scores'
    
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    game_name = Column(String, nullable=False)
    score = Column(Integer, nullable=False)
    
    player = relationship("Player", back_populates="scores")
    
    @classmethod
    def create(cls, player_id, game_name, score):
        session = Session()
        try:
            score_obj = cls(player_id=player_id, game_name=game_name, score=score)
            session.add(score_obj)
            session.commit()
            return score_obj
        finally:
            session.close()
    
    @classmethod
    def get_leaderboard(cls, game_name, limit=10):
        session = Session()
        try:
            from sqlalchemy import func
            return session.query(
                Player.username,
                func.max(cls.score).label('high_score')
            ).join(Player).filter(
                cls.game_name == game_name
            ).group_by(Player.username).order_by(
                func.max(cls.score).desc()
            ).limit(limit).all()
        finally:
            session.close()
    
    @classmethod
    def get_all(cls):
        session = Session()
        try:
            return session.query(cls).all()
        finally:
            session.close()

class Game(Base):
    __tablename__ = 'games'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    category = Column(String, nullable=False)
    
    @classmethod
    def create(cls, name, category):
        session = Session()
        try:
            game = cls(name=name, category=category)
            session.add(game)
            session.commit()
            game_id = game.id
            return game_id
        except Exception:
            session.rollback()
            return None
        finally:
            session.close()
    
    @classmethod
    def get_all(cls):
        session = Session()
        try:
            return session.query(cls).all()
        finally:
            session.close()
    
    @classmethod
    def find_by_name(cls, name):
        session = Session()
        try:
            return session.query(cls).filter_by(name=name).first()
        finally:
            session.close()