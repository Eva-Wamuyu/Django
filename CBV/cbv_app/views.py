from django.shortcuts import render
from django import views
from .forms import *

# Create your views here.

class FormView(views.View):
  def get(self,request,*args,**kwargs):
    form = UserForm()
    return render(request,'form.html',{'form':form})
  
  def save_img(name,file):
    url = f"data/pics/{name}"
    with open(url,'wb+') as opened:
      for info in file.chunks():
        opened.write(info)

  
  def post(self, request,*args,**kwargs):
    form = UserForm(request.POST,request.FILES)
    print(request.POST)
    print(form.errors)
    if form.is_valid():
      #FormView.save_img(form.photo,request.FILES['photo'])
      form.save()
      form = UserForm()
      return render(request,'form.html',{'form':form})
    return render(request,'form.html',{'form':form})


class UpdateForm(views.View):
  def get(self, request, *args, **kwargs):
    pass




