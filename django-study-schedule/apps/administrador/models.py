from markdownx.models import MarkdownxField
from core.models import BaseModel
from django.db import models

class MyModel(BaseModel):
    titulo = models.CharField(blank=False, null=True, max_length=30)
    myfield = MarkdownxField()