from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Task
from .serializers import TaskSerializer


# Create your views here.

# HOME VIEW
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'admin_panel': 'admin/',
        'all_tasks': 'tasks/',
        'get_specific_task': 'tasks/<id>/getOne',
        'add_new_task': 'tasks/create',
        'edit_one_task': 'tasks/<id>/edit',
        'delete_one_task': 'tasks/<id>/delete'
    }
  
    return Response(api_urls)


# CREATE NEW TASK
@api_view(['POST'])
def addNewTask(request):
    newTask = TaskSerializer(data=request.data)
    
    # # validating for already existing data
    # if Task.objects.filter(**request.data).exists():
    #     raise serializers.ValidationError('Task already exist')
    
    if newTask.is_valid():
        newTask.save()
        return Response(data=newTask.data, status=status.HTTP_201_CREATED)
    
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# VIEW ONE TASK
@api_view(['GET'])
def getOneTask(request, pk):
    print('GET ONE TASK')
    try:
        task = Task.objects.get(pk=pk)
        print('THIS IS THE TASK')
        print(task)
        print('THIS IS THE SERIALIZED TASK')
        serialized = TaskSerializer(task)
        print(serialized)
        return Response(data=serialized.data, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
   