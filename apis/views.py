# apis/views.py
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics, viewsets

from todos.models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['title']
    search_fields = ['title', 'description']

    def get_queryset(self):
        queryset = Todo.objects.all()

        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title=title)

        return queryset


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
