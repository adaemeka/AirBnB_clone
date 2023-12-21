#!/usr/bin/python3
"""Creates the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review class."""

    place_id = ""
    user_id = ""
    text = ""
