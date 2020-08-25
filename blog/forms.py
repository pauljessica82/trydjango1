from django import forms 

from .models import Article 
class ArticleForm(forms.ModelForm): 
	title		= forms.CharField(label='' , widget=forms.TextInput(attrs={"placeholder": "Your title"}))
	content = forms.CharField(required=True, 
		label='' , widget=forms.Textarea(
			attrs={
			"placeholder": "Your content" ,
			"class": "new-class-name two",
			"id": "my-id-for-textarea",
			"rows": 7,
			"cols" : 40
				}
				))

	
	class Meta:
		model = Article
		fields = [ 
		'title', 
		'content', 
		'active'
	    ]