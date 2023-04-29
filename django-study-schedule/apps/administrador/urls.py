from django.urls import path

from . import views

app_name = "administrador"

urlpatterns = [                
        path('models/', views.MyListView.as_view(), name='models-list'),
        path('models/create/', views.MyCreateView.as_view(), name='models-create'),
        path('models/<uuid:uuid>/update', views.MyUpdateView.as_view(), name='models-update'),
]
