from django.shortcuts import render
from .forms import AuthorForm

# Create your views here.

def simple_file(request):
  form = AuthorForm()

  
  
  return render(request, 'file_app/index.html',{'form':form})