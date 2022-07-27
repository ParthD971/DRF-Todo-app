# apis/urls.py
from django.urls import path, include

from .views import ListTodo, DetailTodo, TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TodoViewSet, basename='todos')

urlpatterns = [
    path('', ListTodo.as_view()),
    path('router/', include(router.urls)),
    path('<int:pk>/', DetailTodo.as_view()),
]

