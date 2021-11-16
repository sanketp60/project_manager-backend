from django.db import models
from django.utils import timezone
from shortuuidfield import ShortUUIDField
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

class Project(models.Model):
    ProjectID = ShortUUIDField(primary_key=True)
    ProjectName = models.CharField(max_length=100)
    ProjectDescription = models.TextField()
    ProjectDuration = models.CharField(max_length=5)
    ProjectAvatar = models.ImageField(upload_to='project_manager_app', storage=gd_storage, blank=True)

    def __str__(self):
        return f'{self.ProjectName} ({self.ProjectID})'

class Task(models.Model):
    TaskID = ShortUUIDField(primary_key=True)
    TaskName = models.CharField(max_length=100)
    TaskDescription = models.TextField()
    TaskStartDate = models.DateField(default=timezone.now)
    TaskEndDate = models.DateField(default=timezone.now)
    Project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.TaskName} ({self.TaskID})'
