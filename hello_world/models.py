from django.db import models
from uuid import uuid4


# Create your models here.
class Grid(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.TextField(blank=True)
    

