from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(verbose_name='Benutzername', max_length=64)
    
    class Meta:
        verbose_name = 'Blog Kategorie'
        verbose_name_plural = ' Blog Kategorien'

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, verbose_name='Benutzer', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Kategori', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Title', max_length=64)
    content = models.TextField(verbose_name='Inhalt', )
    created_date = models.DateTimeField(verbose_name='Schaffung D.', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Aktualisierung D.', auto_now=True)
    
    class Meta:
        verbose_name = 'Blogeintrag'
        verbose_name_plural = 'Blogeinträge'

    def __str__(self):
        return self.category + ' / ' + self.title











