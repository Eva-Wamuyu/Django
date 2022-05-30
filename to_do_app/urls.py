from django.urls import path



from .views import *

urlpatterns = [
  path('',index,name='index'),
  path('<int:day>',the_task, name="task_day"),
  path('<day>',the_task,name="task_day"),
  
]