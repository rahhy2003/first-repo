from django.urls import path
from .views import health

app_name = "inventory"

urlpatterns = [
    path("health/", health, name="health"),
]


