from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


#cara lama bukan pakai template
def index2(request):
    return HttpResponse('<h1>Halo Dunia</h1>')

def about2(request):
    return HttpResponse('ini about')
    