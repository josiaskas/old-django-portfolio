from django.shortcuts import render, get_object_or_404
from .models import Project, Article, Podcast, Book, Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ContactForm

#event
from events.contact import ContactMadeEvent


# Create your views here.

def index(request):
    projects = Project.objects.filter(featured = True, published =True)[:6]
    articles = Article.objects.order_by('pub_date')[:3]
    podcasts = Podcast.objects.order_by('pub_date')[:3]
    books = Book.objects.order_by('post_date')[:6]

    context = {
        'projects' : projects,
        'articles' : articles,
        'podcasts' : podcasts,
        'books' : books
    }
    return render(request,'index.html',context)

def contact(request):
    form = ContactForm
    context ={
        'form' : form
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid() :
            context['valid_form'] = True
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            amount = form.cleaned_data['amount']
            project_type = form.cleaned_data['project_type']
            details = form.cleaned_data['details']
            #we create a contact
            Contact.objects.create(
                name=name,
                email=email,
                amount=amount,
                project_type=project_type,
                details=details
            )
            ContactMadeEvent(
                name=name,
                email=email,
                budget=amount,
                project_type=project_type
            )

        else:
            context['valid_form'] = False
            context['errors'] = form.errors.items()

    #we put the form with errors inside the context
    context['form'] = form
        

    return render(request,'contact.html',context)

def projectsIndex(request): 
    query = request.GET.get('query')
    message = 'no search'
    search_succes = False

    if not query:
        projects_list = Project.objects.filter(published=True)
        projects_paginator = Paginator(projects_list,15)
    else :
        #first we search by project name
        projects_list = Project.objects.filter(name__icontains = query)
        search_succes = True
        message = 'search made and {} found'.format(len(projects_list))

        #if fnothing we search by excerpt
        if not projects_list.exists():
            projects_list = Project.objects.filter(excerpt__icontains = query)
            message = 'search made and {} found'.format(len(projects_list))
            #if nothing we just return a sorry message
            if not projects_list.exists():
                projects_list = Project.objects.filter(published=True)
                message = 'no result'
                search_succes = False
        
        projects_paginator = Paginator(projects_list,15)
        

    page = request.GET.get('page')

    try:
        projects = projects_paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = 1
        projects = projects_paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = projects_paginator.num_pages
        projects = projects_paginator.page(page)
    
    context = {
        'projects' : projects,
        'page' : page,
        'message' : message,
        'search_succes' :  search_succes,
        'query' : query
    }

    return render(request,'projects/index.html',context)

def projectsShow(request,slug):
    project = get_object_or_404(Project,slug=slug)
    context = {
        'project' : project,
    }
    return render(request,'projects/show.html',context)
