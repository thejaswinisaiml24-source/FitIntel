from database.models import Base
from database.db_connection import engine

Base.metadata.create_all(bind=engine)

print("Database Created Successfully")