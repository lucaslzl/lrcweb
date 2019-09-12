from django.shortcuts import render
from django.conf import settings
import os

from mainsite.models import *


def index(request):
    return render(request, 'mainsite/index.html')


def people(request):
    prof = People.objects.filter(type='Professors').order_by('name')
    pos = People.objects.filter(type='Pos-doc students').order_by('name')
    phd = People.objects.filter(type='PhD students').order_by('name')
    msc = People.objects.filter(type='MSc students').order_by('name')
    collab = People.objects.filter(type='Collaborators').order_by('name')
    under = People.objects.filter(type='Undergraduate students').order_by('name')
    alumni = People.objects.filter(type='Alumni').order_by('name', 'title')
    context = {'people': people,
               'prof': prof,
               'pos': pos,
               'phd': phd,
               'msc': msc,
               'collab': collab,
               'under': under,
               'alumni': alumni}
    return render(request, 'mainsite/people.html', context)


def research(request):
    research = ResearchTopics.objects.all().order_by('name')
    curr_projects = Projects.objects.filter(state='Current')
    past_projects = Projects.objects.filter(state='Past').order_by('year')
    thesis = OnGoingThesis.objects.all().order_by('professor')
    context = {
        'research': research,
        'curr': curr_projects,
        'past': past_projects,
        'thesis': thesis
    }
    return render(request, 'mainsite/research.html', context)


def publications(request):
    book = Book.objects.filter(type='Book').order_by('-year')
    book_chapter = Book.objects.filter(type='Book Chapter').order_by('-year')

    int_journal = Journal.objects.filter(type='International Journal').order_by('-year')
    braz_journal = Journal.objects.filter(type='Brazilian Journal').order_by('-year')
    
    int_conference = Conference.objects.filter(type='International Conference').order_by('-year')
    braz_conference = Conference.objects.filter(type='Brazilian Conference').order_by('-year')
    
    doc_thesis = Thesis.objects.filter(type='Doctorate Thesis').order_by('-year')
    ms_thesis = Thesis.objects.filter(type='Master Thesis').order_by('-year')
    
    tech_reports = TechnicalReports.objects.all().order_by('-year')
    rec_awards = RecognitionAwards.objects.all().order_by('-year')
    context = {
        'book': book,
        'book_chapter': book_chapter,
        'int_journal': int_journal,
        'braz_journal': braz_journal,
        'int_conference': int_conference,
        'braz_conference': braz_conference,
        'doc_thesis': doc_thesis,
        'ms_thesis': ms_thesis,
        'tech_reports': tech_reports,
        'rec_awards': rec_awards
    }
    return render(request, 'mainsite/publications.html', context)


def tools(request):
    tool = Tools.objects.all().order_by('name')
    context = {
        'tools': tool
    }
    return render(request, 'mainsite/tools.html', context)


def videos(request):
    video = Videos.objects.all().order_by('name')
    context = {
        'videos': video
    }
    return render(request, 'mainsite/videos.html', context)


def contact(request):
    return render(request, 'mainsite/contact.html')


def clean(request):
    people = People.objects.all()
    pic_list = []
    for p in people:
        if str(p.picture) != '':
            pic_list = pic_list + [str(p.picture).replace('photos/', '')]

    full_url = settings.MEDIA_ROOT + '/photos'
    for file in os.listdir(full_url):
        if str(file) not in pic_list:
            os.remove(settings.MEDIA_ROOT + '/photos/' + str(file))

    pub = Publications.objects.all()
    pdf_list = []
    for p in pub:
        if str(p.pdf) != '':
            pdf_list = pdf_list + [str(p.pdf).replace('pdfs/', '')]

    full_url = settings.MEDIA_ROOT + '/pdfs'
    for file in os.listdir(full_url):
        if str(file) not in pdf_list:
            os.remove(settings.MEDIA_ROOT + '/pdfs/' + str(file))

    return render(request, 'mainsite/clean.html')
