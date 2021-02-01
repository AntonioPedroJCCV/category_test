from typing import Type


def validate_type(key: str, value: object, type: Type) -> object:
    if not isinstance(value, type):
        raise TypeError(f"{key.capitalize()} must be {type}!")
    return value

def validate_not_empty(key: str, value: str) -> str:
    if not value.strip():
        raise ValueError(f"{key.capitalize()} cannot be empty!")
    return value

def validate_len(key: str, value: object, max_len: int) -> object:
    if len(value) > max_len:
        raise ValueError(f"{key.capitalize()} cannot be greater than {max_len} characters!")
    return value
