from django.urls import path
from todoapp.views import todo_list, todo_detail
urlpatterns = [
    path('', todo_list, name="todo_list"),
    path('task_detail/<str:pk>', todo_detail, name="todo_detail"),
]