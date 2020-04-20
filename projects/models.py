import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    name = models.CharField(verbose_name="Nom",max_length=40)
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(verbose_name="Nom",max_length=40)
    picture = models.ImageField("Image", upload_to="projects/", height_field=None, width_field=None, max_length=None)
    logo_picture = models.ImageField("logo", upload_to="projects/", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    excerpt = models.CharField("extrait", max_length=300, default="A simple project")
    content = models.TextField("contenue")

    url = models.URLField("Url vers le projet", max_length=200)
    slug = models.CharField("slug",max_length=100,unique=True)

    featured = models.BooleanField("en vedette", default=False)
    published = models.BooleanField("publié", default=False)
    tags =  models.ManyToManyField(Tag, related_name='projects')
    realease_date = models.DateField(verbose_name="Date de livraison")
    def __str__(self):
        return self.name

    def was_release_this_year(self):
        return self.realease_date >= timezone.now() - datetime.timedelta(year=1)



class Contact(models.Model):

    PROJECTS_TYPES = (
        ('web app','Web App'),
        ('web site','Web site'),
        ('Ios app','Ios App'),
    )
    name = models.CharField(verbose_name="Nom",max_length=60)
    email = models.EmailField(verbose_name="Email adress",max_length=254)
    project_type = models.CharField(verbose_name="Type de projet",choices=PROJECTS_TYPES,max_length=20)
    amount = models.FloatField(verbose_name="Montant",default=300)
    details = models.TextField(verbose_name="Détails additionel", max_length=2000)
    def __str__(self):
        return f'{self.name} - {self.project_type}'

class Podcast(models.Model):
    title = models.CharField("title",max_length=100)
    source = models.CharField("source",max_length=100)
    embed_code = models.TextField("code", max_length=500)
    pub_date = models.DateField(verbose_name="Date de publication")

    def __str__(self):
        return self.title
    

class Book(models.Model):
    title = models.CharField("Book name", max_length=100)
    author = models.CharField("auteur",max_length=100)
    content = models.TextField("contenu", max_length=500, null=True, blank=True)
    embed_code = models.TextField("code",max_length=1000)
    post_date = models.DateTimeField("Date du post",auto_now=True)

    def __str__(self):
        return self.title
    

class Article(models.Model):
    title = models.CharField("title",max_length=100)
    author = models.CharField("auteur",max_length=100)
    content = models.TextField("contenu", max_length=500)
    link = models.URLField("lien vers l'article",max_length=200)
    pub_date = models.DateField("Date de publication", auto_now=True)

    def __str__(self):
        return self.title
    