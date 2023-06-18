import datetime 
import os
import random
import string

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


"""
<QueryDict: {'csrfmiddlewaretoken': ['Qy6CudhNE4xvolYcWpVOt6qjkVTTPzJtGwTj7Jm6wfJNVM3Re9CIc7dSLpmRnn4k'],
 'quiz': ['26'], 
 'content': ['<p>mnasndnmasd</p>\r\n'], 'explanation': ['<p>aksdjaskdasd</p>\r\n'], 
 'choice_order': ['random'], 'choice_set-TOTAL_FORMS': ['5'], 
 'choice_set-INITIAL_FORMS': ['0'], 'choice_set-MIN_NUM_FORMS': ['0'],
  'choice_set-MAX_NUM_FORMS': ['1000'],
   'choice_set-0-choice': ['nzmzxmcmzxc'], 
   'choice_set-1-choice': ['sanmdasdas'], 
   'choice_set-2-correct': ['on'], 
   'choice_set-2-choice': ['wqkeqwe'],
    'choice_set-3-choice': [''], 
    'choice_set-4-choice': ['']}>

<QueryDict: {'csrfmiddlewaretoken': ['ESDLwpuQOf6iycKTLrEQgDlY1mBZxXEfuQqs9Vz9GqiA5DPy3blKZE8xsQ4X5LZ6'], 
'quiz': ['27'], 'content': ['<p>&nbsp;mnmansmndmnasd</p>\r\n'], 
'explanation': ['qmwnemnqwe'], 'choice_order': ['random'], 
'choice_set-TOTAL_FORMS': ['5'], 'choice_set-INITIAL_FORMS': ['0'],
 'choice_set-MIN_NUM_FORMS': ['0'], 'choice_set-MAX_NUM_FORMS': ['1000'],
  'choice_set-0-correct': ['on'], 'choice_set-0-choice': ['qmwnemnqwe'],
   'choice_set-1-choice': [''], 'choice_set-2-choice': [''],
    'choice_set-3-choice': [''], 'choice_set-4-choice': ['']}>
"""