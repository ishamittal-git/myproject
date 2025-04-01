from django.urls import path
from .views import factories_list  # ✅ Corrected function name

urlpatterns = [
    path('factories/', factories_list, name='factory_list'),  # ✅ Use the correct function
]
