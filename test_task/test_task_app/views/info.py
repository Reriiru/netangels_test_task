from django.views.generic.detail import DetailView

from test_task_app.models import ShortenedUrl


class InfoView(DetailView):
    template_name = "info.html"
    model = ShortenedUrl

    def get_context_data(self, **kwargs):
        context = super(InfoView, self).get_context_data(**kwargs)
        return context
