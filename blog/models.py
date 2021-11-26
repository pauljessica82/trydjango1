from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def get_absolute_url(self):  # method should be done by default in model
        return reverse("article-detail",
                       kwargs={"my_id": self.id})  # pk is also known as id field , so id = pk

    def my_stuffs(self):
        return {
            'id': self.id,
            'content': self.content
        }

