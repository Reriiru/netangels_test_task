from test_task_app.models import ShortenedUrl
from django.views.generic import ListView


class PopularView(ListView):
    model = ShortenedUrl
    template_name = 'popular.html'
    context_object_name = 'shortened_list'
    paginate_by = 20
    queryset = ShortenedUrl.objects.order_by('-hits', '-creation_date')
