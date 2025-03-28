from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy's Base object
Base = declarative_base()

# Database URL (for SQLite in this example)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create an engine that connects to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal is used to create sessions that are tied to a particular database connection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# This will create all tables defined in your models
Base.metadata.create_all(bind=engine)
