
from django.urls import path ,include
from .views import user_list, profile_detail
urlpatterns = [
    path('', user_list, name= 'users'),
    path('user/<int:pk>/', profile_detail, name= 'users_detail'),
]

