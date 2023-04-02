from django.apps import AppConfig
from django.core.signals import setting_changed

def myallback(sender, **kwargs):
    print("Setting changed")

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
