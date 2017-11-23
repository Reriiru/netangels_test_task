from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from test_task_app.forms import ShortenerForm
from test_task_app.models import ShortenedUrl


def shortener_view(request):

    if request.method == 'POST':
        form = ShortenerForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('info', slug=post)
    else:
        form = ShortenerForm()

    display_urls = ShortenedUrl.objects.order_by('-hits',
                                                 '-creation_date')[0:20]

    template = loader.get_template('shortener.html')
    context = {
        'form': form,
        'urls': display_urls
    }

    return HttpResponse(template.render(context, request))