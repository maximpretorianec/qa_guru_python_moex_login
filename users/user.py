from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: datetime
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str
