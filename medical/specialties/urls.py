from . import views
from django.urls import path

urlpatterns = [
    path("", views.specialties, name="specialties"),
    path("delete_specialty/<int:id>", views.delete_specialty, name="delete_specialty"),
]