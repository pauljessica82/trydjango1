from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    HyperlinkedModelSerializer,
    CharField
)
from blog.models import Article


# class PostCreateSerializer(ModelSerializer):
#     class Meta:
#         model = Article
#         fields = [
#             # "user",
#             "title",
#             "content",
#             "active"
#         ]


class PostSerializer(HyperlinkedModelSerializer):
    image = SerializerMethodField()
    user = CharField(source='user.username', read_only=True)
    url = HyperlinkedIdentityField(view_name="post-detail")

    class Meta:
        model = Article
        fields = ['id',
                  'url',
                  'user',
                  'content',
                  'image',
                  'active']

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image
