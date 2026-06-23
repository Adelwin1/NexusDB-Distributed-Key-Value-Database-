from sqlalchemy.orm import Session
from app.models.ticket import Ticket
from app.services.ml_service import classify_ticket
from app.services.ai_logic import generate_resolution


def create_ticket(db: Session, title: str, description: str):
    # 1. classify ticket
    category = classify_ticket(title, description)

    # 2. generate AI resolution
    resolution = generate_resolution(category, title, description)

    # 3. store ticket
    ticket = Ticket(
        title=title,
        description=description,
        category=category,
        resolution=resolution
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return ticket


def get_all_tickets(db: Session):
    return db.query(Ticket).all()