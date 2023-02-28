from django.urls import path
from .views import index, new_data, devices, add_device, delete_device

urlpatterns = [
    path("", index, name="index"),
    path("data/<str:id>/<int:m>", new_data, name="data"),
    path("devices", devices, name="devices"),
    path("add_device/<str:id>", add_device, name="add_devices"),
    path("delete_device/<str:id>", delete_device, name="delete_device"),
]