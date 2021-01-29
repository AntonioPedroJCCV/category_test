from sqlalchemy import Column, String
from sqlalchemy.orm import validates
from back.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column('name', String(length=100), nullable = False)
    description = Column('description', String(length=255), nullable = True)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description


    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError("The name must be a string")
        if not name.strip():
            raise ValueError("The name can't be empty")
        if len(name) > 100:
            raise ValueError("The name can't exceed 100 characters")
        return name


    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError("The description must be a string!")
        if len(description) > 255:
            raise ValueError("The description can't exceed 255 or less characters!")
        return description
