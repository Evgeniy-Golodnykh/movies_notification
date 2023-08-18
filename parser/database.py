import logging

from configs import POSTGRES_DB
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()


class Movie(Base):
    """Movie model."""

    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True)
    url = Column(String(200))

    def __repr__(self):
        return self.name


def add_to_db(item):
    """Add Movie instance to database."""

    logging.info(URL.create(**POSTGRES_DB))
    engine = create_engine(URL.create(**POSTGRES_DB))
    Base.metadata.create_all(engine)
    session = Session(engine)
    name, url = item
    if session.query(Movie).filter(Movie.name == name).count():
        return False
    session.add(Movie(name=name, url=url))
    session.commit()
    session.close()
    return True
