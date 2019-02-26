from .base import *


# Activate Django-Heroku.
django_heroku.settings(locals(), databases=False)
