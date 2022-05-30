from django.urls import path

from . import views

urlpatterns = [
  path("simple_file",views.simple_file,name="simple_field")
    


]
