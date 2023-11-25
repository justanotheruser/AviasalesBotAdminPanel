import datetime

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"
    user_id: int | None = Field(default=None, primary_key=True)


class FlightDirection(SQLModel, table=True):
    __tablename__ = "flight_directions"
    id: int | None = Field(default=None, primary_key=True)
    start_code: str
    start_name: str
    end_code: str
    end_name: str
    with_transfer: bool
    departure_at: str
    return_at: str | None
    price: float | None
    last_update: datetime.datetime


class UserDirection(SQLModel, table=True):
    __tablename__ = "users_directions"
    user_id: int = Field(nullable=False, primary_key=True, foreign_key="users.user_id")
    direction_id: int = Field(
        nullable=False, primary_key=True, foreign_key="flight_directions.id"
    )
