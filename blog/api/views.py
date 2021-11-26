from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)
from .serializers import PostDetailSerializer, PostListSerializer, PostCreateSerializer

from blog.models import Article


class PostCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDetailSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDetailSerializer


class PostListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = PostListSerializer


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDetailSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
