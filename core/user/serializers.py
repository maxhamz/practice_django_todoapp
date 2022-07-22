# core/user/serializers.py

from core.user.models import User
from task.models import Task
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'created', 'updated', 'tasks']
        read_only_field = ['is_active', 'created', 'updated']
