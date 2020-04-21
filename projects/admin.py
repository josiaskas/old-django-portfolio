from django.contrib import admin
from .models import Project, Tag, Book, Article, Contact, Podcast
# Register your models here.

admin.site.register(Tag)
admin.site.register(Book)
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(Podcast)

def make_published(modeladmin, request, queryset):
    queryset.update(published=True)
make_published.short_description = "Rendre public le projet"

def make_private(modeladmin, request, queryset):
    queryset.update(published=False)
make_private.short_description = "Rendre privé le projet"

def make_featured(modeladmin, request, queryset):
    queryset.update(featured=True)
make_featured.short_description = "Mettre en première page"

def duplicate_project(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.name = object.name+'-copy'
        object.slug = object.slug+'-copy'
        object.published = False
        object.save()
duplicate_project.short_description = "Dupliquer le projet"

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'published','featured']
    ordering = ['realease_date']
    actions = [make_published, make_private, make_featured, duplicate_project]

admin.site.register(Project, ProjectAdmin)