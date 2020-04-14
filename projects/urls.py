from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('projects/',views.projectsIndex,name='projects.index'),
    path('projects/<slug:slug>',views.projectsShow,name='projects.show')
]