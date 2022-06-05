from django.db import models

from .base_model import BaseModel
from .room import Room
from user.models import User


class RoomJoin(BaseModel):
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roomJoin", db_column="email")
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="roomJoin", db_column="room_id")

    class Meta:
        db_table = "roomJoin"
