from django.urls import path
from .views import Home, TaskDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
]