from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gerar/", views.gerar, name="gerar_nickname"),
]
