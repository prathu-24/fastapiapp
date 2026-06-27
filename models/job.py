from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import declarative_base,relationship
from models.company import Company

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False,index=True)
    email = Column(String,index=True,unique=True)
    phone = Column(String,index=True,unique=True)
    description = Column(String)
    salary = Column(Integer)
    company_id = Column(Integer,ForeignKey("companies.id"))
    company = relationship ("Company",back_populates="jobs")

