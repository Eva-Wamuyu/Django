from django.db import models

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255, unique=True)
  cv = models.FileField(upload_to='media/doc')
  photo = models.ImageField(upload_to='media/photo')



  def __str__(self):
    return f"name: {self.name}, email: {self.email}"
  