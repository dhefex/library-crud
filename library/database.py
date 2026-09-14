
DATABASE_URL = "mysql+pymysql://nodeuser:123456@localhost/library"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)