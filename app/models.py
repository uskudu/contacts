from sqlalchemy.orm import Mapped, mapped_column

from app import database as _database


class Contact(_database.Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str]
    phone_number: Mapped[str]
    # timestamp: Mapped[TIMESTAMP] = mapped_column(
    #     TIMESTAMP, server_default=func.now(), nullable=False
    # )
