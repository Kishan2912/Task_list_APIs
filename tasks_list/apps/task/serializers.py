from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        error_messages = {'name': {'required': 'cannot be blank or null'}} 
