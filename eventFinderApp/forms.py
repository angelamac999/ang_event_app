from django import forms
from django.forms import ModelForm
from .models import Event, Category
from django.contrib.admin import widgets
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class EventForm(forms.ModelForm):
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

    # def clean_renewal_date(self):
    #     data = self.cleaned_data['renewal_date']
        
    #     # Check if a date is not in the past. 
    #     if data < datetime.date.today():
    #         raise ValidationError(_('Invalid date - event in past'))

    #     # Check if a date is in the allowed range (+4 weeks from today).
    #     if data > datetime.date.today() + datetime.timedelta(weeks=52):
    #         raise ValidationError(_('Invalid date - renewal more than 52 weeks ahead'))

    #     # Remember to always return the cleaned data.
    #     return data


class EditEventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
                 'title',
                 'venue',            
        ]


# class DateInput(forms.DateInput):
#  input_type = 'date'