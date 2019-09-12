from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# python3 manage.py makemigrations mainsite
# python3 manage.py sqlmigrate mainsite ####
# python3 manage.py migrate


'''
    People of the lab comprehending students, professors, and collaborators.
    Fields 'project', 'year', and 'title' are only for alumni.
'''


class People(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, null=True, blank=True)
    site = models.CharField(max_length=50, null=True, blank=True)
    lattes = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to='photos/')
    advisor = models.ForeignKey("self", null=True, blank=True, on_delete=models.DO_NOTHING)
    types = (('Alumni', 'Alumni'), ('Collaborators', 'Collaborators'),
             ('MSc students', 'MSc students'), ('Pos-doc students', 'Pos-doc students'),
             ('PhD students', 'PhD students'), ('Professors', 'Professors'),
             ('Undergraduate students', 'Undergraduate students'))
    type = models.TextField(choices=types, default='Alumni')

    project = models.CharField(max_length=200, null=True, blank=True)
    year = models.PositiveIntegerField('Alumni Year',
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)], null=True, blank=True)
    titles = (('Master', 'Master'), ('Doctor', 'Doctor'), ('Pos-doc', 'Pos-doc'))
    title = models.TextField('Alumni Title', choices=titles, null=True, blank=True)

    def __str__(self):
        return self.name

'''
    Publications of the laboratory.
    Reference has to be at citation format.
    Publications are divided into: Books, Journal, Conference, Thesis, Technical Reports,
    Recognition Awards.
    Books, Journal, Conference: uses national or international distinction, year, 
    and reference.
    Thesis: uses title distinction, and fields reference and year.
    Technical reports: uses reference (name), authors, abstract, year, and pdf file (if needed).
    Recognition awards: uses reference and year.
'''

class Book(models.Model):
    reference = models.TextField()
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)], null=True, blank=True)
    types = (('Book', 'Book'), ('Book Chapter', 'Book Chapter'))
    type = models.CharField(max_length=50, choices=types)

    def __str__(self):
        return self.reference


class Journal(models.Model):
    reference = models.TextField()
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)], null=True, blank=True)
    types = (('Brazilian Journal', 'Brazilian Journal'),
            ('International Journal', 'International Journal'))
    type = models.CharField(max_length=50, choices=types)

    def __str__(self):
        return self.reference


class Conference(models.Model):
    reference = models.TextField()
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)], null=True, blank=True)
    types = (('Brazilian Conference', 'Brazilian Conference'),
            ('International Conference', 'International Conference'))
    type = models.CharField(max_length=50, choices=types)

    def __str__(self):
        return self.reference


class Thesis(models.Model):
    reference = models.TextField()
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)], null=True, blank=True)
    types = (('Doctorate Thesis', 'Doctorate Thesis'),
             ('Master Thesis', 'Master Thesis'))
    type = models.CharField(max_length=50, choices=types)

    def __str__(self):
        return self.reference


class TechnicalReports(models.Model):
    reference = models.TextField()
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)], null=True, blank=True)
    authors = models.CharField(max_length=200, null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    pdf = models.FileField(null=True, blank=True, upload_to='pdfs/')

    def __str__(self):
        return self.reference


class RecognitionAwards(models.Model):
    reference = models.TextField()
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)], null=True, blank=True)

    def __str__(self):
        return self.reference


'''
    The name of the research interests.
'''


class ResearchTopics(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


'''
    Projects are divided into current and past.
    Current: uses sponsored or internationally sponsored, name, sponsor.
    Past: uses mainly name, sponsor, year, abstract.
'''


class Projects(models.Model):

    name = models.CharField(max_length=200)
    abstract = models.TextField(null=True, blank=True)
    sponsor = models.CharField(max_length=100, null=True, blank=True)
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)], null=True, blank=True)
    types = (('Sponsored Research', 'Sponsored Research'),
             ('International Cooperation Sponsored Research',
              'International Cooperation Sponsored Research'))
    type = models.CharField(max_length=50, choices=types)
    states = (('Current', 'Current'), ('Past', 'Past'))
    state = models.CharField(max_length=10, choices=states, default='Current')

    def __str__(self):
        return self.name


'''
    Ongoing thesis. 
    Listed sorted by professor.
'''


class OnGoingThesis(models.Model):
    name = models.CharField(max_length=100)
    professor = models.ForeignKey(People, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


'''
    Tools developed or used by researchers on the lab.
'''


class Tools(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name


'''
    Videos of tools developed or used by researchers on the lab.
'''


class Videos(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name
