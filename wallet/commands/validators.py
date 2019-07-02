from django.core.exceptions import ValidationError
from registration.models import Profile


def crw_address(value):
    if not value.startswith("CRW"):
        raise ValidationError('La direccion de envio debe empezar por CRW')
