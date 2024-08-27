
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('tasks',views.tasksPage,name='tasksPage'),
    path('tasks/createTask',views.createTask,name='createTask'),
    path('tasks/<int:id>',views.taskDetails,name='taskDetails'),
    path('tasks/<int:id>/complete',views.completeTask,name='completeTask'),
    path("tasks/<int:id>/delete",views.deleteTask,name='deleteTask'),
    path('tasks/terminadas',views.tasks_terminadas,name='tasks_terminadas'),
]