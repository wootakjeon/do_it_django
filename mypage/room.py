from .models import BaseModel
from django.db import models


class Room(BaseModel):
    room_id = models.IntegerField()

    class Meta:
        db_table = "room"
