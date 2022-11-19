from django.urls import path
from .views import *

urlpatterns = [
    path('get/', GetList.as_view()),
    path('post/', CreateTask.as_view()),
    path('get/<int:pk>/', GetTask.as_view()),
    path('update/<int:pk>/', UpdateTask.as_view()),
    path('delete/<int:pk>/', DeleteTask.as_view()),
    path('multipost/', CreateMultiTask),
    path('multidelete/<str:pk_ids>/', DeleteMultiTask.as_view()),
]