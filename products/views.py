from django.shortcuts import render, get_object_or_404, redirect
from .models import product
from .forms import ProductForm, RawProductForm
# Create your views here.

# def product_create_view(request):
# 	my_form = RawProductForm() # created an instance of the form

# 	if request.method == "POST":
# 		my_form = RawProductForm(request.POST)  
	
# 	if my_form.is_valid():
# 		print (my_form.cleaned_data)
# 		product.objects.create(**my_form.cleaned_data)
# 	else:
# 		print(my_form.errors)

# 	context = {
# 	"form": my_form

# 	}
# 	return render(request, "products/product_create.html", context)


# def product_create_view(request):
# 	# print(request.GET)
# 	# print(request.POST) 
		#if request.method == "POST" :
		#my_new_title = request.POST.get('title')
		#print(my_new_title)
		#Product.objects.create(title=my_new_title)
# 	context = {}
# 	return render(request, "products/product_create.html", context)

def product_list_view(request): 

	queryset = product.objects.all()

	context = {
	"object_list" : queryset
	}

	return render( request , "products/product_list.html", context)

def product_delete_view(request, id):
	obj = get_object_or_404(product, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context =  {
	"object": obj 

	}

	return render(request, "products/product_delete.html", context)



def product_create_view(request):

	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm
	

	context = {
		'form': form
	}
	
	
	return render(request, "products/product_create.html", context)



def dynamic_lookup_view(request, id):
	# obj = product.objects.get(id=id)
	obj = get_object_or_404(product, id=id)
	context =  {
	"object": obj 

	}
	return render( request, "products/product_detail.html", context)




