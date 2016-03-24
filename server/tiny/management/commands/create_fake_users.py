import urllib2
import json

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Generate users from randomuser.me'

    def add_arguments(self, parser):
        parser.add_argument('user_count', nargs='+', type=int)

    def handle(self, *args, **options):
        response = urllib2.urlopen(
            'http://api.randomuser.me/?results={}'.format(options['user_count'][0])
        )
        data = json.load(response)
        for userItem in data['results']:
            userJ = userItem['user']
            user = User.objects.create_user(
                userJ['username'], userJ['email'], userJ['password'],
                first_name=userJ['name']['first'], last_name=userJ['name']['last']
            )
            user.save()
