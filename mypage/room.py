from .base_model import BaseModel
from django.db import models


class Room(BaseModel):
    class Meta:
        db_table = "room"
