from django.urls import path
from .views import Individuals


urlpatterns = [
    path('api/individuals', Individuals.as_view(), name="individuals")
]
