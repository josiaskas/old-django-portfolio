import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    name = models.CharField(verbose_name="Nom",max_length=40)
    picture = models.URLField("image", max_length=200)
    content = models.TextField("contenue")
    realease_date = models.DateField(verbose_name="Date de livraison")
    url = models.URLField("Url", max_length=200)

    def __str__(self):
        return f'Le projet : {self.name}'

    def was_release_this_year(self):
        return self.realease_date >= timezone.now() - datetime.timedelta(year=1)

class Tag(models.Model):
    name = models.CharField(verbose_name="Nom",max_length=40)
    project = models.ManyToManyField(Project,related_name='project')
    def __str__(self):
        return f'Tag : {self.name}'
