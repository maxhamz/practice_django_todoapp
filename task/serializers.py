from rest_framework import serializers
from .models import Task
from core.user.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    taskmaster = UserSerializer(read_only=True)
    
    class Meta:
        model = Task
        read_only_fields = ['id', 'created_at', 'last_modified_at']
        fields = '__all__'
