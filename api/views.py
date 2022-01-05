from django.shortcuts import render

from rest_framework import generics ,permissions

from .serializers import TodoSerializer,TodoCompleteSerializer

from todo.models import Todo

#from api import serializers

from django.utils import timezone
# Create your views here.

class TOdoCompletedList(generics.ListAPIView):
    serializer_class = TodoSerializer

    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        user = self.request.user 

        return Todo.objects.filter(user=user ,datecompleted__isnull =False).order_by('-datecompleted')


class TodoListcreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer

    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        user = self.request.user 

        return Todo.objects.filter(user=user ,datecompleted__isnull =True)


    def perform_create(self,serializer):
        serializer.save(user=self.request.user) 

class TOdoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer

    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        user = self.request.user 

        return Todo.objects.filter(user=user )

class TOdoComplete(generics.UpdateAPIView):
    serializer_class = TodoCompleteSerializer

    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        user = self.request.user 

        return Todo.objects.filter(user=user )

    def perform_update(self,serializer):
        serializer.instance.datecompleted =timezone.now() 
        serializer.save()