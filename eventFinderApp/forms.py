from django import forms
from django.forms import ModelForm
from .models import Event, Category
from django.contrib.admin import widgets


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
           'title',
           'venue',
           'location',
           'start_time',
           'end_time',
           'categories',
           'host',
           ]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # self.fields['start_time'].widget = widgets.AdminDateWidget()
        # self.fields['end_time'].widget = widgets.AdminTimeWidget()
        self.fields['start_time'].widget = widgets.AdminSplitDateTime()
        self.fields['end_time'].widget = widgets.AdminSplitDateTime()


class EditEventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
                 'title',
                 'venue',            
        ]


# class DateInput(forms.DateInput):
#  input_type = 'date'