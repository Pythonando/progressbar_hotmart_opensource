from django.apps import AppConfig
from django.contrib.auth import get_user_model

class ProgressbarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'progressbar'