from django.urls import path
from .views import get_info,get_person

urlpatterns = [
    path('', get_info, name='get_info'),
    path('2/', get_person, name='get_person'),
]