from django.contrib import admin
from django.urls import path


from pages.views import (
home_view, 
contact_view, 
about_view

)


app_name = 'pages'
urlpatterns = [
    
    path('home/', home_view),
    path('contact/', contact_view) ,
    path('about/', about_view),
   
   

   ]
   