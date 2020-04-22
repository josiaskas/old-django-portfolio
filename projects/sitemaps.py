from django.contrib.sitemaps import Sitemap
from .models import Project
from django.urls import reverse

class ProjectSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Project.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.realease_date

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'contact', 'projects.index']

    def location(self, item):
        return reverse(item)