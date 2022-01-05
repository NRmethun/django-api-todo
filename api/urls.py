from django.urls import path
from . import views 
urlpatterns = [
    path('todos', views.TodoListcreate.as_view()),
    path('todos/<int:pk>', views.TOdoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TOdoComplete.as_view()),
    path('todos/completed', views.TOdoCompletedList.as_view()),
]