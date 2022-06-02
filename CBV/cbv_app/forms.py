from django.forms import ModelForm
from .models import User



class UserForm(ModelForm):
  class Meta:
    model = User
    #fields = ['name','photo', 'email', 'userName']
    fields = "__all__"



    #if yu wnt to override the labels - the ffield names
    labels = {
      'name': 'What is your name',
    }

