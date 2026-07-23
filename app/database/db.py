from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
DATABASE_URL="postgresql://anshika:1234@localhost:5432/knowledgeos_db"
engine = create_engine(DATABASE_URL)
sessionLocal=sessionmaker(bind=engine)

def get_db():
	db=SessionLocal()

	try:
		yield db 
	finally:
		db.close()
