import json

from django.http import JsonResponse
from django.views.generic import View

from .models import MyUser as User
from .utils import id_generator
from redis_init import redis


class TinyView(View):
    def get(self, request, tiny_id):
        user_id = redis.get('tiny_user_{}'.format(tiny_id))
        user = User.objects.get(pk=user_id)
        link = redis.get('tiny_link_{}'.format(tiny_id))
        return JsonResponse({'link': link, 'user': user.id})

    def post(self, request, tiny_id):
        json_data = json.loads(request.body)
        tiny_id = id_generator()
        link = json_data['link']
        random_user = User.objects.random()

        # We can use setex for expired raw
        exist_link = redis.get('tiny_link_{}'.format(link))
        if exist_link:
            tiny_id = exist_link
        redis.set('tiny_user_{}'.format(tiny_id), random_user.id)
        redis.set('tiny_link_{}'.format(json_data['link']), tiny_id)
        redis.set('tiny_id_{}'.format(tiny_id), json_data['link'])

        return JsonResponse({'tinyId': tiny_id})
