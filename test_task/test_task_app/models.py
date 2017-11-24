import datetime

from django.db import models
from django.core.validators import URLValidator


class ShortenedUrl(models.Model):
    original_url = models.TextField(max_length=2100)
    shortened_uri = models.CharField(max_length=20, unique=True)
    hits = models.IntegerField(default=0)
    creation_date = models.DateField(default=datetime.date.today)
    slug = models.SlugField(max_length=20)
