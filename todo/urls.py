from django.urls import path
from . import views


from .views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask, UserLogin, RegisterView
from django.contrib.auth.views import LogoutView

app_name = 'todo'

urlpatterns = [
    path('login/', UserLogin.as_view(), name="login"),
    #path('logout/', LogoutView.as_view(next_page="todo:login"), name="logout"),
    path('logout/', views.logout_user, name='logout'),
    path('register', RegisterView.as_view(), name="register"),
    path('', TaskList.as_view(), name="tasks_list"),
    path('task_detail/<int:pk>/', TaskDetail.as_view(), name="task_detail"),
    path('create_task/', CreateTask.as_view(), name='create_task'),
    path("update_task/<str:pk>/", UpdateTask.as_view(), name='update_task'),
    path('delete_task/<str:pk>/', DeleteTask.as_view(), name='delete_task'),
]
