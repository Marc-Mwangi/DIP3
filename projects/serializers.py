from rest_framework import serializers
from .models import  Project

#Using Model serializer to reduce redudndacy
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        #Model beig used
        model= Project
        #Fields required
        fields = ('id','project_name','desc','user')
    