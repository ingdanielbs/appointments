from . import views
from django.urls import path

urlpatterns = [
    path("", views.patients, name="patients"),
    path("delete_patient/<int:id>", views.delete_patient, name="delete_patient"),
    path("edit_patient/<int:id>", views.edit_patient, name="edit_patient"),
]