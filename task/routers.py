# task/routers.py
from django.urls import path
from task.views import ApiOverview, addNewTask, getOneTask, getTasksList, taskDelete, taskEdit

urlpatterns = [
    path('overview', ApiOverview, name="task-home"),
    path('create', addNewTask, name='create-task'),
    path('getList', getTasksList, name='task-lists'),
    path('getOne/<int:pk>', getOneTask, name='retrieve-task'),
    path('drop/<int:pk>', taskDelete, name='drop-task'),
    path('edit/<int:pk>', taskEdit, name='edit-task'),
]
