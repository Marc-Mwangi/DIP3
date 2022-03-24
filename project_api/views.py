from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Profile
from .serializers import UserSerializer
# Create your views here.
#Function based API views
def user_list(request):
    
    if request.method == "GET":
        #Query all users from databse
        users= Profile.objects.all()
        serializer = UserSerializer(users, many=True)
        
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return JSONParser(serializer.data, status=201)
        
        return JsonResponse(serializer.errors,status=400)
