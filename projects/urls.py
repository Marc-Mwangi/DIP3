
from django.urls import path ,include
from .views import  project_list
urlpatterns = [
    path('projects/', project_list, name= 'project'),
]