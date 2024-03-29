from django.urls import path
from .views import TaskView, TaskDetailView


urlpatterns = [
    path('tasks/', TaskView.as_view(), name='tasks'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='tasks-detail'),
]
