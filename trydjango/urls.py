from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/blog/', include('blog.api.urls')),
    path('products/', include('products.urls')),
    path('blog/article/', include('blog.urls', namespace="blog")),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('pages.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('courses/', include('courses.urls')),

]
