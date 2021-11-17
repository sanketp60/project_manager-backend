from .models import Project
from .models import Task
from .serializers import ProjectListSerializer, TaskListSerializer
from .serializers import ProjectSerializer, TaskSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date

def datechecker(startdate, enddate):
    sdate = date(
        int(startdate.split("-")[0]),
        int(startdate.split("-")[1]),
        int(startdate.split("-")[2])
        )
    edate = date(
        int(enddate.split("-")[0]),
        int(enddate.split("-")[1]),
        int(enddate.split("-")[2])
        )
    if sdate>edate:
        return False
    else:
        return True

class ProjectList(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectListSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProjectDetail(APIView):
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskList(APIView):
    def get(self, request, pk, format=None):
        tasks = Task.objects.all().filter(Project=pk)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        request.data["Project"]=pk
        serializer = TaskSerializer(data=request.data)
        if datechecker(request.data["TaskStartDate"],request.data["TaskEndDate"])==False:
            return Response("Start Date should come before or on the end date", status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        if datechecker(request.data["TaskStartDate"],request.data["TaskEndDate"])==False:
            return Response("Start Date should come before or on the end date", status=status.HTTP_400_BAD_REQUEST)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response("Task Deleted",status=status.HTTP_204_NO_CONTENT)


