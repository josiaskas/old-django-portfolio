from django.contrib import admin
from .models import Project, Tag, Book, Article, Contact, Podcast
# Register your models here.

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Book)
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(Podcast)