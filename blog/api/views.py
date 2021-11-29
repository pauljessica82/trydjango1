from django.db.models import Q

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.filters import (
    OrderingFilter,
    SearchFilter
)
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from .serializers import PostSerializer
# , PostListSerializer, PostCreateSerializer,
from .permissions import IsOwnerOrReadOnly
from blog.models import Article


# class PostCreateAPIView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = PostCreateSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

#
#
# class PostListAPIView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = PostListSerializer
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ['title', 'content', 'user__first_name']
#     pagination_class = PostPageNumberPagination
#
#     def get_queryset(self, *args, **kwargs):
#         queryset_list = Article.objects.all()
#         query = self.request.GET.get('q')
#         if query:
#             queryset_list = queryset_list.filter(
#                 Q(title__icontains=query) |
#                 Q(content__icontains=query) |
#                 Q(user__first_name__icontains=query) |
#                 Q(user__last_name__icontains=query)
#             ).distinct()
#         return queryset_list
#
#
# class PostUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = PostDetailSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#
#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)
#

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Article.objects.all()

