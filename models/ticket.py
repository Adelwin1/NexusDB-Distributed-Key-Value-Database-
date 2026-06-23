from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.core.database import Base

priority = Column(String, default="low")
status = Column(String, default="open")


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    # basic ticket data
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)

    # AI classification
    category = Column(String, nullable=True)

    # AI / RAG fields
    embedding = Column(Text, nullable=True)

    # AI-generated output
    resolution = Column(Text, nullable=True)

    # metadata
    created_at = Column(DateTime, default=datetime.utcnow)