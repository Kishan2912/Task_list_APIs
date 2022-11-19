from rest_framework import serializers
from .models import * # import models

# Create your Serializer here.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task # define the model for Serializer
        fields = "__all__" # write down fields of model

