from django.urls import path
from .views import TodoListCreateView, TodoRetrieveUpdateDestroyView

urlpatterns = [
    path('', TodoListCreateView.as_view(), name='create_list_todo'),
    path('<int:pk>/', TodoRetrieveUpdateDestroyView.as_view(), name='retrieve_update_destroy_todo'),
]
