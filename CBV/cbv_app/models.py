from django.db import models


# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=120)
  photo = models.ImageField(upload_to="data/pics/")
  email = models.EmailField(max_length=120)
  userName = models.CharField(max_length=120, unique=True)


  def __str__(self):
    return f"{self.name} ({self.email})"



