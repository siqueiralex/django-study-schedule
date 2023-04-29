from django.forms.widgets import ClearableFileInput, SplitDateTimeWidget, DateInput, TimeInput

from markdownx.widgets import MarkdownxWidget

class CustomMarkdownxWidget(MarkdownxWidget):
    template_name = 'core/widgets/markdownx_widget.html'
    