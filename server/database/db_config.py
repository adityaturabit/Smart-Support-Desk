# import sessionmaker from sqlalchemy.orm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


db_url = f"mysql+pymysql://root:root@localhost:5432/smart_desk"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)


