from . import views
from django.urls import path

urlpatterns = [
    path("", views.doctors, name="doctors"),
    path("delete_doctor/<int:id>", views.delete_doctor, name="delete_doctor"),
    path("edit_doctor/<int:id>", views.edit_doctor, name="edit_doctor"),
]