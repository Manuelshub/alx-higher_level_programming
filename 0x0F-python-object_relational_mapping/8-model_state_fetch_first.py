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

    for state in session.query(State).order_by(State.id).first():
        print("{}: {}".format(state.id, state.name))

    session.close()
