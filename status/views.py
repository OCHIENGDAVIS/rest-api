from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication

from .models import Status
from .serializers import StatusSerializer


class StatusListAPIView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusCreateAPIView(generics.CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (BasicAuthentication, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
