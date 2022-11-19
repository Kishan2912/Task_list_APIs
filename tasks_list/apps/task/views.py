# import different views
# using django rest framework
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# import serializers and models
from .serializers import *
from .models import *

# Create your views here.
# View for push List of tasks
class GetListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# View for create a task
class CreateTaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# View for push only one task with thier id
class GetTaskView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# View for update a task
class UpdateTaskView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# View for delete a task
class DeleteTaskView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# View for create multiple task at once
@api_view(['POST'])
def CreateMultiTaskView(request):
    serialized = TaskSerializer(data=request.data,many=True)
    if serialized.is_valid(raise_exception=True):
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
    
# View for delete multiple task at once with their ids
class DeleteMultiTaskView(APIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def delete(self,request,pk_ids):
        ids = [int(pk) for pk in pk_ids.split(',')]
        for i in ids:
            get_object_or_404(Task, pk=i).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
