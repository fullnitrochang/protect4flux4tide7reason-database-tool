from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_connection(connection_string):
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    return Session()