from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.generics import RetrieveAPIView
from .models import AppInfo
from .serializers import AppInfoSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AppInfoView(RetrieveAPIView):
    queryset = AppInfo.objects.all()
    serializer_class = AppInfoSerializer

    def get_object(self):
        return AppInfo.objects.first()