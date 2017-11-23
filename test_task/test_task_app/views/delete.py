from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from test_task_app.models import ShortenedUrl


class UrlDelete(DeleteView):
    model = ShortenedUrl
    success_url = reverse_lazy('shortener-form')
    template_name = 'delete.html'