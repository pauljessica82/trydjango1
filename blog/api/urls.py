from django.contrib import admin
from django.urls import path

from blog.api.views import (
    # PostCreateAPIView,
    PostViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = router.urls

# old = [
#
#     path('l/', PostListAPIView.as_view(), name='article-list'),
#     # how to pass slug and make it work
#     path('<int:pk>/', PostDetailAPIView.as_view(), name='api-detail')
#     # # Generic detail view ArticleDetailView must be called with either an object pk or a slug in the URLconf.
#     path('create/', PostCreateAPIView.as_view(), name='article-create'),
#     path('<int:pk>/update/', PostUpdateAPIView.as_view(), name='article-update'),
#     path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='article-delete')
#
# ]
