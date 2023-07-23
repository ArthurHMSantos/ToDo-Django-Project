from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('task_detail/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('task_form/', views.TaskCreate.as_view(), name='task_form'),
    path('task_update/<int:pk>/', views.TaskUpdate.as_view(), name='task_update'),
    path('task_delete/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),
]