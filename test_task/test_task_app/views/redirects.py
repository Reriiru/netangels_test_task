from django.shortcuts import redirect

from test_task_app.models import ShortenedUrl


def redirect_view(request, slug):

    media = ShortenedUrl.objects.get(shortened_uri=slug)

    media.hits += 1

    redirect_url = media.original_url
    media.save()

    return redirect(redirect_url)
