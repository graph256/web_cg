from django import forms
from django.db import transaction

from .models import NewsAndEvents, Session, Semester, SEMESTER
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# news and events
class NewsAndEventsForm(forms.ModelForm):
    summary = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = NewsAndEvents
        fields = ('title', 'summary', 'posted_as',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control'})
        self.fields['posted_as'].widget.attrs.update({'class': 'form-control'})


class SessionForm(forms.ModelForm):
    next_session_begins = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'type': 'date',
            }
        ),
        required=True)

    class Meta:
        model = Session
        fields = ['session', 'is_current_session', 'next_session_begins']


class SemesterForm(forms.ModelForm):
    semester = forms.CharField(
        widget=forms.Select(
            choices=SEMESTER,
            attrs={
                'class': 'browser-default custom-select',
            }
        ),
        label="Семестр",
    )
    is_current_semester = forms.CharField(
        widget=forms.Select(
            choices=((True, 'Да'), (False, 'Нет')),
            attrs={
                'class': 'browser-default custom-select',
            }
        ),
        label="текущий семестр ?",
    )
    session = forms.ModelChoiceField(
        queryset=Session.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'browser-default custom-select',
            }
        ),
        label="Сессия",
        required=True
    )

    next_semester_begins = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
            }
        ),
        label="Начало следующего семестра",
        required=True)

    class Meta:
        model = Semester
        fields = ['semester', 'is_current_semester', 'session', 'next_semester_begins']
