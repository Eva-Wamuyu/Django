from django.shortcuts import render
from django.http import HttpResponse, Http404
from .logic.to_do import *

# Create your views here.

def index(request):
  return render(request, 'to_do/index.html',{'to_do_list':to_do_list})

def the_task(request,day):
  if type(day) == int:
    days = ["sun","mon","tue","wed","thu","fri","sat"]
    try:
      day = days[day]
    except IndexError:
      return HttpResponse("<h2 class='text-center text-danger'>Invalid day</h2>")
  else:
    day = day.lower()
    day = day[:3]
    print(type(day))
  try:
    task = to_do_list[day]
  except (KeyError):
    return HttpResponse("<h2 class='text-center text-danger'>Invalid day</h2>")
  return render(request, 'to_do/to_do.html',{'to_do':task,'day':day})


def the_task2(request,day):


  

   return render(request, 'to_do/to_do.html',{'to_do':task,'day':day})

  
   
    

    
    
   


def getDay(day):
    day = day.lower()
    return day

# def the_task(request,day):
#     # day=''
#     if day== '0' or day.lower()=='monday' or day.lower()=='mon':
#         day='mon'
#     elif day=='1' or day.lower()=='tuesday' or day.lower()=='tue':
#         day='tue'
#     elif day=='2' or day.lower()=='wednesday' or day.lower()=='wed':
#         day='wed'
#     elif day=='3' or day.lower()=='thursday' or day.lower()=='thu':
#         day='thu'
#     elif day=='4' or day.lower()=='friday' or day.lower()=='fri':
#         day='fri'
#     elif day=='5' or day.lower()=='saturday' or day.lower()=='sat':
#         day='sat'
#     elif day=='6' or day.lower()=='sunday' or day.lower()=='sun':
#         day='sun'
#     else:
#         return 
#     return render(request,"to_do/to_do.html",{"day":day,"to_do":to_do_list[day]})


# def int_the_tasks(request,day):
#   days = ["sun","mon","tue","wed","thu","fri","sat"]
#   day = days[day]
#   print("Thhhhhhhhhhhhhhhhhhhhhhhhhh")
#   print(days)
#   return render(request,"to_do/to_do.html",{"day":day,"to_do":to_do_list[day]})

  






