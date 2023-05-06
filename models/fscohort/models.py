from django.db import models

class Student(models.Model):
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   email = models.EmailField()
   number = models.IntegerField()
   is_active = models.BooleanField(default=True)
   #image = models.ImageField()
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)


   def __str__(self):
      return f'{self.first_name} {self.last_name} # {self.number}'
   
   class Meta: # change default settings
      verbose_name = 'student'
      verbose_name_plural = 'Students'
      ordering = ['number']