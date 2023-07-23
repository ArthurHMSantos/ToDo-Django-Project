from django.urls import path
from .views import Home, TaskCreate, TaskDetail, TaskUpdate

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('task_detail/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task_form/', TaskCreate.as_view(), name='task_form'),
    path('task_update/<int:pk>/', TaskUpdate.as_view(), name='task_update')
]