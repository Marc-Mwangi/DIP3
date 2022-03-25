from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Project
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def project_list(request):
    
    if request.method == "GET":
        #Query all users from databse
        projects= Project.objects.all()
        serializer = UserSerializer(projects, many=True)
        
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return JSONParser(serializer.data, status=201)
        
        return JsonResponse(serializer.errors,status=400)

