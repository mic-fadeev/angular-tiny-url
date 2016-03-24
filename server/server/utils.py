import string
import random
from redis_init import redis


def _id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    repeat = True
    while repeat:
        unique_id = _id_generator(size, chars)
        print(unique_id)
        if not redis.get('tiny_{}'.format(unique_id)):
            repeat = False
    return unique_id
