# TODO: Implement Routings Here
from django.urls import path
from todolist.views import delete, change,add_task, register, show_todolist, login_user, logout_user

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('create-task/', add_task, name = 'add_task' ),
    path('delete/<int:pk>', delete, name='delete'),
    path('change/<int:pk>', change, name='change'),
]