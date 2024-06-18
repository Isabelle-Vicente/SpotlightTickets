# home/adapters.py
from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError

class CustomAccountAdapter(DefaultAccountAdapter):
    def authenticate(self, request, **credentials):
        user = super().authenticate(request, **credentials)
        if user and not user.is_staff:
            raise ValidationError("Apenas usuários com permissão de staff podem fazer login.")
        return user
