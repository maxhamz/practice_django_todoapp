from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from django.utils import timezone
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
        'drop_one_task': 'tasks/<id>/drop'
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
    try:
        task = Task.objects.get(pk=pk)
        serialized = TaskSerializer(task)
        return Response(data=serialized.data, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# VIEW TASK LIST
@api_view(['GET'])
def getTasksList(request):
    tasks = Task.objects.all()
    serialized = TaskSerializer(tasks, many=True)
    return Response(data=serialized.data, status=status.HTTP_200_OK)


# DROP ONE TASK
@api_view(['DELETE'])
def taskDelete(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# EDIT ONE TASK
@api_view(['PUT'])
def taskEdit(request, pk):
    noEditFields = ["id", "created_at", "last_modified_at"]
    try:
        editForm = request.data
        for i in editForm.keys():
            if i in noEditFields:
                errorMessage = "FORBIDDEN EDIT FIELD: %s" % (i)
                return Response(data=errorMessage, status=status.HTTP_400_BAD_REQUEST)
        
        task = Task.objects.get(pk=pk)
        taskInJSON = TaskSerializer(task).data
        editForm['last_modified_at'] = timezone.now()
        
        
        # REPLACE EACH FIELD IN TASK WITH THE ONES IN EDITFORM
        for f in editForm.keys():
            taskInJSON[f] = editForm[f]

        serialized = TaskSerializer(instance=task, data=taskInJSON)
        if serialized.is_valid():
            serialized.save()
            return Response(data=serialized.data, status=status.HTTP_200_OK)
        else:
            return Response(data='INVALID EDIT FORM ENTRY', status=status.HTTP_400_BAD_REQUEST)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
