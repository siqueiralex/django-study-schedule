from django.views.generic import ListView, UpdateView, View, CreateView
from django.urls import reverse
from .models import MyModel
from .forms import MyForm
from core.views import UUIDViewMixin


class MyListView(ListView):
    model = MyModel
    template_name = "administrador/list.html"

class MyCreateView(CreateView):
    model = MyModel
    form_class = MyForm
    template_name = "administrador/form.html"
    
    def get_success_url(self) -> str:
        return reverse("administrador:models-list")

class MyUpdateView(UUIDViewMixin, UpdateView):
    model = MyModel
    form_class = MyForm
    template_name = "administrador/form.html"
    uuid_url_kwarg = "uuid"
    
    def get_success_url(self) -> str:
        return reverse("administrador:models-list")
