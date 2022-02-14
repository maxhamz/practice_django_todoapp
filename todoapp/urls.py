"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todoapp_backend.views import ApiOverview, addNewTask, getOneTask, getTasksList, taskDelete, taskEdit
# from todoapp_backend.views import TaskList, TaskDetail

urlpatterns = [
    path('', ApiOverview, name='home'),
    path('admin/', admin.site.urls, name='admin_portal'),
    path('tasks/create', addNewTask, name='create-task'),
    path('tasks/getList', getTasksList, name='task-lists'),
    path('tasks/<int:pk>/getOne', getOneTask, name='retrieve-task'),
    path('tasks/<int:pk>/drop', taskDelete, name='drop-task'),
    path('tasks/<int:pk>/edit', taskEdit, name='edit-task'),
    # path('tasks/getList/', TaskDetail.as_view(), name='task_detail'),
    # path('tasks/', TaskList.as_view(), name='task_list'),
]
