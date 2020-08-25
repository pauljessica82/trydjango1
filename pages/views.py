from django.shortcuts import render

from django.http import HttpResponse


def home_view(request, *args,**kwargs):
    
	my_home_dictionary = { 
		"heading" : "Hello World", 
	}
	print (args, kwargs) 
	print (request.user)
	#return HttpResponse("<h1>Hello World</h1>") # string of html code
	return render(request, "home.html", my_home_dictionary) 

def contact_view(request,*args,**kwargs):
	#return HttpResponse("<h1>Contact Page</h1>") # string of html code
	return render(request, "contact.html", {})

def about_view(request,*args,**kwargs):
	#return HttpResponse("<h1>About Page</h1>") # string of html code
	my_context = {
		"my_text": "First word in my dictionary",
		"this_is_true" : True, 
		"my_number" : 9256 , 
		"my_list" : [123,345,312,250, "jess"]
		}
	return render(request, "about.html", my_context)

# Create your views here.
