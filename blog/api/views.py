from django.db.models import Q

from rest_framework.filters import (
    OrderingFilter,
    SearchFilter
)
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer
from blog.models import Article


# class PostCreateAPIView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = PostCreateSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Article.objects.all()

