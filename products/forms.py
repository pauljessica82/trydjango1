from django import forms 

from .models import product 
class ProductForm(forms.ModelForm): 
	title		= forms.CharField(label='' , widget=forms.TextInput(attrs={"placeholder": "Your title"}))
	email 		= forms.EmailField()
	description = forms.CharField(required=False, 
		label='' , widget=forms.Textarea(
			attrs={
			"placeholder": "Your description" ,
			"class": "new-class-name two",
			"id": "my-id-for-textarea",
			"rows": 7,
			"cols" : 40
				}
				))
    
	price 		= forms.DecimalField( initial=199.99)

	def clean_title(self, *args, **kwargs): 
		title = self.cleaned_data.get("title")
		if not "CFE" in title: 
			raise forms.ValidationError("This is not a valid title")
		if not "news" in title: 
			raise forms.ValidationError("This is not a valid title")
		return title

	def clean_email(self, *args , **kwargs):
		email = self.cleaned_data.get("email")
		if not email.endswith("edu"):
			raise forms.ValidationError("This is not a valid email")
		return email 

	class Meta:
		model = product
		fields = [ 
		'title', 
		'description',
		'price'
	    ]

class RawProductForm(forms.Form): 
	title		= forms.CharField(label='' , widget=forms.TextInput(attrs={"placeholder": "Your title"}))
	description = forms.CharField(required=False, 
		label='' , widget=forms.Textarea(
			attrs={
			"placeholder": "Your description" ,
			"class": "new-class-name two",
			"id": "my-id-for-textarea",
			"rows": 15,
			"cols" : 50
				
		}




			))
	price 		= forms.DecimalField( initial=199.99)
