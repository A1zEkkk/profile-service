from .base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, VARCHAR, Numeric
from decimal import Decimal




class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    surname: Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    phone: Mapped[str] = mapped_column(VARCHAR(30), nullable=False, unique=True)
    balance: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=Decimal("0.0"))
