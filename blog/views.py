from django.shortcuts import render

# Create your views here test
def index(request):
    return render(request,'blog.html')
