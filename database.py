from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

Base = declarative_base()

url = "postgresql+psycopg2://user:password@localhost/dbname"