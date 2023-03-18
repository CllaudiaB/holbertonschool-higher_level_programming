#!/usr/bin/python3
"""
that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_add = State(name="Louisiana")
    session.add(state_to_add)
    session.commit()
    print("{}".format(state_to_add.id))
    session.close()
