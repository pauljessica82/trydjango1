from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Article
from .forms import ArticleForm

from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView

)


# Create your views here.
class ArticleListView(ListView):
    template_name = "articles/article_list.html"  # this overrides <blog>/ <modelname>.html
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("my_id")
        return get_object_or_404(Article, id=id_)

    def get_context_data(self, **kwargs):
        silly_message = self.kwargs.get('message')
        original_context = super(ArticleDetailView, self).get_context_data(**kwargs)
        original_context['silly_message'] = self.request.GET.get('q')
        return original_context


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)  # will post cleaned data in terminal
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)  # this method grabs the object or instance were trying tochange


class ArticleDeleteView(DeleteView):
    template_name = "articles/article_delete.html"
    queryset = Article.objects.all()  # not necessary because of getobject method below

    def get_object(self):  # get that object in the database
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')

    # def article_create_view(request):

# 	form = ArticleForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = ArticleForm


# 	context = {
# 		'form': form
# 	}


# 	return render(request, "articles/article_create.html", context)

# def article_list_view(request): 

# 	queryset = Article.objects.all()

# 	context = {
# 	"object_list" : queryset
# 	}

# 	return render( request , "articles/article_list.html", context)

# def dynamic_lookup_view(request, id):
# 	# obj = product.objects.get(id=id)
# 	obj = get_object_or_404(Article, id=id)
# 	context =  {
# 	"object": obj 

# 	}
# 	return render( request, "articles/article_detail.html", context)
