from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path('factories/', views.factories_list, name='factory_list'),
    path('factories/<int:id>/', views.all_detail, name='all_detail'),
]
