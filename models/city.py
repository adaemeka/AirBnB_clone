#!/usr/bin/python3
"""Creates the City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city"""

    state_id = ""
    name = ""
