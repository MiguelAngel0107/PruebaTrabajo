from django.urls import path
from .views import CalculateNumberEndBaterias, ConfigVariableView

urlpatterns = [
    path("input-data/", CalculateNumberEndBaterias.as_view()),
    path('new-config/', ConfigVariableView.as_view())
]
