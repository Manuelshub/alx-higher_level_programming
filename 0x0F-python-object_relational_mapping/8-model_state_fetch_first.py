#!/usr/bin/python3
"""
This Script prints the first State object from a database
"""

if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Create engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Creating session
    Session = sessionmaker(engine)
    session = Session()

    state = session.query(State).filter(State.id == 1).first()
    print(state)
