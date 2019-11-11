from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    categories = models.ManyToManyField('Category', related_name='events')
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events', blank=True)
    # image = models.ImageField(upload_to='profile_image', blank=True)

    # email = models.ForeignKey(email, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
