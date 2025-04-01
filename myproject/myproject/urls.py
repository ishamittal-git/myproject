from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('edible.urls')),  # Include the edible app's URLs
    path('admin/', admin.site.urls),
]
