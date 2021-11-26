from rest_framework.serializers import ModelSerializer

from blog.models import Article


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            # "user",
            "title",
            "content",
            "active"
        ]


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "user",
            "title",
            "content",
            "active"
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "active"
        ]

"""

from blog.models import Article
from blog.api.serializers import PostDetailSerializer

data =  {
'title': 'Yeahh buddy', 
'content': 'New content', 
'active': True 
}


"""