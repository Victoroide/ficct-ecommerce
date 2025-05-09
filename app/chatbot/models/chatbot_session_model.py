from django.db import models
from core.models import TimestampedModel
from app.authentication.models import User

class ChatbotSession(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    session_token = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)