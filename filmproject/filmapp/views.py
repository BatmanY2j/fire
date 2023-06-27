from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Film
from .forms import FilmForm
# Create your views here.
def index(request):
    film=Film.objects.all()
    context={
        'movie_list':film
    }
    return render(request,'index.html',context)
def detail(request, movie_id):
    movie=Film.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        movie=Film(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,'add.html')
def update(request,id):
    movie=Film.objects.get(id=id)
    form=FilmForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Film.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')


