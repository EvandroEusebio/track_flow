from track_flow.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import DateTime, func
from sqlalchemy import Integer, String, BigInteger, SmallInteger


class Vehicle(Base):
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(BigInteger,primary_key=True, autoincrement=True)
    plate: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    brand: Mapped[str] = mapped_column(String(100), nullable=False)
    model: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True) , server_default=func.now(), nullable=False)