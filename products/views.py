from django.shortcuts import render, get_object_or_404, redirect
from .models import product
from .forms import ProductForm, RawProductForm
from django.views import View


# Create your views here.

class ProductObjectMixin(object):
    model = product

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None

        if id is not None:
            obj = get_object_or_404(product, id=id)
            return obj


class ProductCreateView(View):
    template_name = 'products/product_create.html'

    def get(self, request):
        form = ProductForm(request.POST)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ProductDetailView(ProductObjectMixin, View):
    template_name = 'products/product_detail.html'

    def get(self, request, id=None, *args, **kwargs):
        context = {'object': self.get_object()}
        # if id is not None:
        #     obj = get_object_or_404(product, id=id)
        #     context['object'] = obj

        return render(request, self.template_name, context)


class ProductUpdateView(View):
    template_name = 'products/product_update.html'
    queryset = product.objects.all()



    def get(self, request, id=None, *args, **kwargs):
        obj = self.get_object()
        context = {}

        if obj is not None:
            form = ProductForm(instance=obj)
            context['object'] = obj
            context['form'] = form

        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        # object not updating
        if obj is not None:

            form = ProductForm(request.POST, instance=obj)

            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form

        return render(request, self.template_name, context)


class ProductDeleteView(View):
    template_name = 'products/product_delete.html'
    queryset = product.objects.all()

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None

        if id is not None:
            obj = get_object_or_404(product, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()

        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()

        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/products/')

        return render(request, self.template_name, context)


class ProductListView(View):
    template_name = 'products/product_list.html'
    queryset = product.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)



