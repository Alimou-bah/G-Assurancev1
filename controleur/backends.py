from django.contrib.auth.backends import BaseBackend
from .models import Controler

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = Controler.objects.get(email=email)
            if user.check_password(password):
                return user
        except Controler.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Controler.objects.get(pk=user_id)
        except Controler.DoesNotExist:
            return None
