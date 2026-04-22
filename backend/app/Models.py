from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Dog(Base):
	__tablename__ = "dogs"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, nullable=False)
	age = Column(Integer, nullable=False)
	breed = Column(String, nullable=False)
	gender = Column(String, nullable=False)
	size = Column(String, nullable=False)
	vaccinated = Column(Boolean, default=False)
	notes = Column(String, nullable=True)

