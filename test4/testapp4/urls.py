from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name=''),

    path('dashboard', views.dashboard, name="dashboard"),

    path('create', views.create, name="create"),

    path('update/<int:pk>', views.update, name='update'),

    path('record/<int:pk>', views.singular, name="record"),

    path('delete/<int:pk>', views.delete, name="delete"),



]