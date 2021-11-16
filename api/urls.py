from django.urls import path
from . import views

urlpatterns = [
    path('projectlist/', views.ProjectList.as_view()),
    path('projectdetail/<str:pk>', views.ProjectDetail.as_view()),
    path('tasklist/<str:pk>', views.TaskList.as_view()),
    path('taskdetail/<str:pk>', views.TaskDetail.as_view()),
]
