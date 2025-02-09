from rest_framework import serializers
from .models import Rest_prac

class RestPracSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rest_prac
        fields = '__all__'
