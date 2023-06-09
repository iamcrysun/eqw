from sqlalchemy import Column, String

from server.src.models.entity import Entity


class User(Entity):
    __tablename__ = "users"

    email = Column(String, index=True, nullable=False)
    username = Column(String, index=True, nullable=False)
    password = Column(String, nullable=False)
