from django.urls import path
from .views import * # import all views

urlpatterns = [
    path('get/', GetListView.as_view()), # get the list of tasks
    path('post/', CreateTaskView.as_view()), # post the task
    path('get/<int:pk>/', GetTaskView.as_view()), # get the specific task
    path('update/<int:pk>/', UpdateTaskView.as_view()), # update the specific task
    path('delete/<int:pk>/', DeleteTaskView.as_view()), # delete the specific task
    path('multipost/', CreateMultiTaskView), # post the multiple task once
    path('multidelete/<str:pk_ids>/', DeleteMultiTaskView.as_view()), # delete the multiple task at once
]