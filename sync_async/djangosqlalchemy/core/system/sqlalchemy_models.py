# core/sqlalchemy_models.py
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Create SQLAlchemy engine
engine = create_engine('mysql+mysqldb://root_user:1234@localhost/syns_async_sqlalchemy_db')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class SQLAUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    email = Column(String(255), unique=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"


# Create function to initialize database
def init_db():
    Base.metadata.create_all(engine)