from django import forms


class AuthorForm(forms.Form):
  name = forms.CharField(max_length=255)
  emails = forms.EmailField(max_length=255)
  image =  forms.ImageField()
  cv = forms.FileField()