from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Profile
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
#Function based API views
@csrf_exempt
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


@csrf_exempt
def profile_detail(request,pk):
    
    try:
        user = Profile.objects.get(pk=pk)
        
    except Profile.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
          data = JSONParser().parse(request)
          serializer = UserSerializer(user,data=data)
          
          if serializer.is_valid():
              serializer.save()
              return JsonResponse(serializer.data, status=201)
          return JsonResponse(serializer.errors, status=400)
    
    elif request.method =='DELETE':
        user.delete()
        return HttpResponse(status=204)
    