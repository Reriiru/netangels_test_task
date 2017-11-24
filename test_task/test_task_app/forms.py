import uuid

from django.forms import ModelForm
from test_task_app.models import ShortenedUrl
from django.core.validators import URLValidator


class ShortenerForm(ModelForm):
    class Meta:
        model = ShortenedUrl
        fields = ['original_url']
    
    def clean_original_url(self):
        original_url = self.cleaned_data.get('original_url')
        validate = URLValidator()
        validate(original_url)
        return original_url

    def save(self):
        media = super(ShortenerForm, self).save(commit=False)
        media.shortened_uri = str(uuid.uuid4())[:20]
        media.hits = 0
        media.slug = media.shortened_uri
        media.save()
        return media.shortened_uri
