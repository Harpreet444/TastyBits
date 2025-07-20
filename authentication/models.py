from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (create_engine, Column, Integer, String, DateTime,
                        ForeignKey, UniqueConstraint)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(PG_UUID(as_uuid=True), primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    
    passwords = relationship("PasswordManager", back_populates="user")
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
    
class PasswordManager(Base):
    __tablename__ = 'passwords'
    
    id = Column(PG_UUID(as_uuid=True), primary_key=True)
    user_id = Column(PG_UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    password_hash = Column(String, nullable=False)
    
    user = relationship("User", back_populates="passwords")
    
    def __repr__(self):
        return f"<PasswordManager(id={self.id}, user_id={self.user_id})>"