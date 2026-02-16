from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgres:******@localhost:5432/dvdrental"


engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(bind=engine)
