#!/usr/bin/python3
"""Creates the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User class."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
