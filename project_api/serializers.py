from rest_framework import serializers
from .models import Profile

#Using Model serializer to reduce redudndacy
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        #Model beig used
        model= Profile
        #Fields required
        fields =('id','picture','user_name','bio','email')
    
    