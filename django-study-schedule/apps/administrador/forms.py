from markdownx.fields import MarkdownxFormField
from django import forms
from .models import MyModel
from core.widgets import CustomMarkdownxWidget

class MyForm(forms.ModelForm):
    myfield = MarkdownxFormField(widget=CustomMarkdownxWidget)
    
    class Meta:
        model = MyModel
        fields = "__all__"