from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Todos
from .serializer import TodosSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class TodoListCreateView(ListCreateAPIView):

    serializer_class = TodosSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user.id)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.id
        return super().create(request, *args, **kwargs)


class TodoRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    serializer_class = TodosSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user.id)
    
