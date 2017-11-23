import datetime
import random
import uuid
from django.core.management.base import BaseCommand

from test_task_app.models import ShortenedUrl


def data_mock():
    shortened_uri = str(uuid.uuid4())[:20]
    input_data = {
        'creation_date': datetime.datetime(2017,
                                           random.randint(1, 12),
                                           1,
                                           10,
                                           10,
                                           10),
        'original_url': 'https://youtube.com/watch?v=tgnsjGGMdxE',
        'shortened_uri': shortened_uri,
        'hits': random.randint(1, 10),
        'slug': shortened_uri
    }
    return input_data


class Command(BaseCommand):
    help = 'Populates DB with test data.'

    def _populate_db(self):
        for index in range(60):
            ShortenedUrl.objects.create(**data_mock())

    def handle(self, *args, **options):
        self._populate_db()
