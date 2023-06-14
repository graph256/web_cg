from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from django.utils.translation import gettext as _
from ckeditor_uploader.fields import RichTextUploadingField

NEWS = "News"
EVENTS = "Events"

POST = (
    (NEWS, "Новость"),
    (EVENTS, "Событие"),
)

FIRST = "First"
SECOND = "Second"


SEMESTER = (
    (FIRST, "Первый"),
    (SECOND, "Второй"),
)


class NewsAndEventsQuerySet(models.query.QuerySet):

    def search(self, query):
        lookups = (Q(title__icontains=query) | 
                  Q(summary__icontains=query) |
                  Q(posted_as__icontains=query)
                  )
        return self.filter(lookups).distinct()


class NewsAndEventsManager(models.Manager):
    def get_queryset(self):
        return NewsAndEventsQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # NewsAndEvents.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().search(query)


class NewsAndEvents(models.Model):
    title = models.CharField(max_length=200, null=True, verbose_name='Название')
    summary = RichTextUploadingField(blank=True, null=True, verbose_name=('Описание'))
    posted_as = models.CharField(choices=POST, max_length=10, verbose_name='Записать как:')
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    upload_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    objects = NewsAndEventsManager()

    def __str__(self):
        return self.title


class Session(models.Model):
    session = models.CharField(max_length=200, unique=True, verbose_name="Сессия")
    is_current_session = models.BooleanField(default=False, blank=True, null=True, verbose_name="Текущая сессия")
    next_session_begins = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.session


class Semester(models.Model):
    semester = models.CharField(max_length=10, choices=SEMESTER, blank=True, verbose_name="Семестр")
    is_current_semester = models.BooleanField(default=False, blank=True, null=True, verbose_name="Текущий семестр")
    session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Сессия")
    next_semester_begins = models.DateField(null=True, blank=True, verbose_name="Начало следующего семестра")

    def __str__(self):
        return self.semester
