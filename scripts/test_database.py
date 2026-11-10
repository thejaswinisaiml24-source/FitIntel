from database.db_connection import SessionLocal
from database.models import DailyActivity

session = SessionLocal()

count = session.query(DailyActivity).count()

print("Total Records:", count)

session.close()