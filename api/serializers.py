from .models import Project
from .models import Task
from rest_framework import serializers

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('TaskID', 'TaskName')

class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('ProjectID', 'ProjectName')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskListSerializer(read_only=True, many=True)
    class Meta:
        model = Project
        fields = '__all__'