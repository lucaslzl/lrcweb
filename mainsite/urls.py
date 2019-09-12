from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('people/', views.people, name='people'),
    path('research/', views.research, name='research'),
    path('publications/', views.publications, name='publications'),
    path('tools/', views.tools, name='tools'),
    path('videos/', views.videos, name='videos'),
    path('contact/', views.contact, name='contact'),
    path('clean/', views.clean, name='clean'),
    url(r'^', views.index, name='index'),
]
