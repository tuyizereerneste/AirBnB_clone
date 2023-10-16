#!/usr/bin/python3
"""Defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents the user class
    Attributes:
        email: Email of the user.
        password: Password of the user.
        first_name: First name of the user.
        last_name: Last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
