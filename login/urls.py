from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("register/", views.register, name="register"),
    path("sign/", views.sign, name="sign"),
    path("exit/", views.exit, name="exit"),
    path("home/", views.home, name="home"),
    path("delete/<int:pk>", views.delete_task, name="delete"),
    path("detail/<int:pk>", views.detail_task, name="detail"),
    path("update/<int:pk>", views.update_task, name="update"),
]
