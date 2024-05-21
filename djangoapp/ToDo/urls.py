from . import views
from django.urls import path

urlpatterns = [
    path("", views.render_to_do, name="to-do"),
]
