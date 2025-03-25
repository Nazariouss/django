from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, AppInfoView  

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('app-info/', AppInfoView.as_view(), name='app-info'),
]
