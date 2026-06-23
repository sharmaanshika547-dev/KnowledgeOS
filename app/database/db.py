from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
DATABASE_URL="postgresql://anshika:1234@localhost:5432/knowledgeos_db"
engine = create_engine(DATABASE_URL)
sessionlocal=sessionmaker(bind=engine)
