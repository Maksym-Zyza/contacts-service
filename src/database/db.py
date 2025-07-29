import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if os.getenv("ENV", "dev") == "dev":
    from dotenv import load_dotenv

    load_dotenv()

username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT")
host = os.getenv("DB_HOST")

url = f"postgresql://{username}:{password}@{host}:{db_port}/{db_name}"

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
