from django.urls import path, re_path
from . import views

urlpatterns = [
    path('todos/', views.todo_list),
    re_path(r'^todos/(?P<task_id>[0-9]+)/$', views.todo_detail),
]