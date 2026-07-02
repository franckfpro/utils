from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('new/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]
