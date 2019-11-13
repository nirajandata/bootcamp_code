from django.shortcuts import render
from .forms import ProductForm , RawProductForm
from .models import Product
# Create your views here.
def product_create_view(request):
    # my_form=ProductForm()
    # if request.method == "POST":
    #     my_form=ProductForm(request.POST)
    #     if my_form.is_valid():
    #      print(my_form.cleaned_data)
    #      Product.objects.create(**my_form.cleaned_data)
    #     else:
    #      print(my_form.errors)
    # context={
    # "form":my_form
    # }
    return render(request,"product_create.html",context)
def product_detail_view(request):
    obj=Product.objects.get(id=1)
    context={
    'object':obj
    }
    return render(request,"product_detail.html",context)