from django.http import HttpResponse
from django.shortcuts import render
def home_view(requests,*args,**kargs):
	#return HttpResponse("<h1 >Nirajan</h1>")
# Create your views here.
	print(requests)
	return render(requests,"home.html",{})
def about_view(requests,*args,**kargs):
	my_context={
	"my_text":"I am a Student",
	"title":"This is a Title",
	"my_number":123,
	"my_list":[123,324,353,535,353],
	"my_html":"<h1>Nirajan Is My Name"
	}
	return render(requests,"about.html",my_context)