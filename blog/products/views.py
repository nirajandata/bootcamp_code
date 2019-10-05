from django.shortcuts import render
from .forms import ProductForm
from .models import Product
# Create your views here.
def product_create_view(request):
	context={
	}
	return render
def product_detail_view(request):
	obj=Product.objects.get(id=1)
	context={
	'object':obj
	}
	return render(request,"product_detail.html",context)