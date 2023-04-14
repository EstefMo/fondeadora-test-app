import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define SQLAlchemy models
Base = declarative_base()


class UrlModel(Base):
    __tablename__ = "urls"
    id = sa.Column(sa.Integer, primary_key=True)
    original_url = sa.Column(sa.String, unique=True)
    shortcode = sa.Column(sa.String, unique=True)


DATABASE_URL = "sqlite:///./urls.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session_from_database():
    if SessionLocal:
        return SessionLocal
    return None
