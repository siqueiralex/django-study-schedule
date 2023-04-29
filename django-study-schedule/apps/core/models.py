import uuid as uuid_lib
from django.db import models

class BaseModel(models.Model):   
    uuid = models.UUIDField(
        unique=True, 
        default=uuid_lib.uuid4, 
        editable=False
    )
    class Meta:
        abstract = True
    