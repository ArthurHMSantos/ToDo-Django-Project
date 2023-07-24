from django.urls import path, include
from . import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.Register.as_view(), name='register'),   

    path('', views.Home.as_view(), name='home'),
    path('task_detail/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('task_form/', views.TaskCreate.as_view(), name='task_form'),
    path('task_update/<int:pk>/', views.TaskUpdate.as_view(), name='task_update'),
    path('task_delete/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),

]