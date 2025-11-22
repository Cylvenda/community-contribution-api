from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)
from rest_framework.viewsets import ModelViewSet
from .serializers import ContributionSerializers, ContributorSerializers
from .models import Contributions, Contributors


class ContributionsViewSet(ModelViewSet):
    serializer_class = ContributionSerializers
    queryset = Contributions.objects.all().order_by("-created_at")
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ["POST", "DELETE", "PUT", "PATCH"]:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_serializers_context(self):
        if self.request.user:
            user = self.request.user
            return {"user": user}
        return None

    def update(self, request, *args, **kwargs):
        contribution = self.get_object()
        if request.user != contribution.user:
            return Response(
                {"error": "Your not permitted to perform this action"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        contribution = self.get_object()
        if request.created_by != contribution.created_by:
            return Response(
                {"error": "Your not permitted to perform this action"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().delete(request, *args, **kwargs)


class ContributorsViewSet(ModelViewSet):
    serializer_class = ContributorSerializers
    queryset = Contributors.objects.all()
    permission_classes = [IsAuthenticated]
