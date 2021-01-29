from sqlalchemy import Column, String
from sqlalchemy.orm import validates
from back.models.base_model import BaseModel

from back.utils.validators import (
    validate_len, 
    validate_not_empty,
    validate_type
)


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column('name', String(length=100), nullable = False)
    description = Column('description', String(length=255), nullable = True)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        name = validate_type(key, name, str)
        name = validate_not_empty(key, name)
        return validate_len(key, name, 100)

    @validates('description')
    def validate_description(self, key, description):
        description = validate_type(key, description, str)
        return validate_len(key, description, 255)
