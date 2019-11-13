from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	title=forms.CharField(required=True)
	description=forms.CharField(label="Info",
			 widget=forms.Textarea(
			 	attrs={
			 	"rows":12,
			 	"cols":14,
			 	"placeholder":"your description"
			 	}
			 	),
			 required=False
			 )
	email=forms.EmailField(label="Enter Your email")
	price=forms.DecimalField(initial=199)
	class Meta:
		model= Product
		fields=[
			'title',
			'description',
			'price',
			'summary',
			
		]
	def clean_title(self,*args,**kwargs):
		title=self.cleaned_data.get("title")
		if "nir" in title:
			return title
		else:
			raise forms.ValidationError("not a valid title")
def clean_emails(self,*args,**kwargs):
		email=self.cleaned_data.get("email")
		if "nir" in email:
			return email
		else:
			raise forms.ValidationError("not a valid title")
class RawProductForm(forms.Form):
			title=forms.CharField(required=True)
			description=forms.CharField(label="Info",
			 widget=forms.Textarea(
			 	attrs={
			 	"rows":12,
			 	"cols":14,
			 	"placeholder":"your description"
			 	}
			 	),
			 required=False
			 )
			price=forms.DecimalField(initial=199)
