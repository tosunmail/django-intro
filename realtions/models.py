from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64) 
    email = models.EmailField(max_length=64) 

    def __str__(self):
        return f'{self.username}'
    
class Profile(models.Model):
    first_name = models.CharField(max_length=64)    
    last_name = models.CharField(max_length=64)    
    about = models.TextField()
    picture = models.ImageField(null=True, blank=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.account} - {self.first_name} - {self.last_name}'