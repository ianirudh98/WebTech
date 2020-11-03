import random
import string
from django.utils.text import slugify
# from .utils import random_string_generator

def random_string_generator(size=10,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_order_generator(instance):
    order_id = random_string_generator(size=10)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_id).exists()
    if qs_exists:
        return unique_order_generator(instance)
    return order_id