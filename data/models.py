from typing import List 


from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin



from data.base import Base


class Tour(Base):
    __tablename__ = "tours"


    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(52))
    description: Mapped[str] = mapped_column(String(520))
    departure: Mapped[str] = mapped_column(String(52))
    picture: Mapped[str] = mapped_column(String(1052))
    price: Mapped[float] = mapped_column()
    stars: Mapped[str] = mapped_column(String(6))
    country: Mapped[str] = mapped_column(String(52))
    nights: Mapped[int] = mapped_column()
    date: Mapped[str] = mapped_column(String(52))

tour_user_assoc = Table(
    "tour_user_assoc",
    Base.metadata,
    Column("tour_id",ForeignKey('tours.id'), primary_key=True),
    Column("user_id",ForeignKey('users.id'), primary_key=True)
)


class User(Base, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(52), unique=True)
    email: Mapped[str] = mapped_column(String(52), unique=True)
    password:Mapped[str] = mapped_column(String(502))
    tour:Mapped[List[Tour]] = relationship(secondary=tour_user_assoc)