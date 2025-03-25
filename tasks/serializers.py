from rest_framework import serializers
from .models import Task
from .models import AppInfo

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

class AppInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppInfo
        fields = '__all__'