from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Author

# Create an SQLite database
engine = create_engine('sqlite:///bookhaven.db', echo=True)

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session for interacting with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example of adding a new author
new_author = Author(first_name='John', last_name='Doe', birth_date='1970-01-01')
session.add(new_author)
session.commit()

print("Database schema created and example data added.")
