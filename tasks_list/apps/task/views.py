from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from .serializers import *
from .models import *

# Create your views here.
class GetList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class GetTask(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UpdateTask(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DeleteTask(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@api_view(['POST'])
def CreateMultiTask(request):
    serialized = TaskSerializer(data=request.data,many=True)
    if serialized.is_valid(raise_exception=True):
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteMultiTask(APIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def delete(self,pk_ids):
        ids = [int(pk) for pk in pk_ids.split(',')]
        for i in ids:
            get_object_or_404(Task, pk=i).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
