from django.contrib import admin
from django.urls import path

from blog.views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView

)

app_name = 'articles'
urlpatterns = [

    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:my_id>/', ArticleDetailView.as_view(), name='article-detail'),
    # Generic detail view ArticleDetailView must be called with either an object pk or a slug in the URLconf.
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete')

]
