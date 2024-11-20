from django.urls import path
from .views import sample_data, index

urlpatterns = [
    path('', index, name="index"),
    path('api/sample/', sample_data),
]