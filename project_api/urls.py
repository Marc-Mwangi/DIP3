
from django.urls import path ,include
from .views import user_list
urlpatterns = [
    path('', user_list, name= 'users'),
]
