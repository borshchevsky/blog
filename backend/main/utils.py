from django.core.exceptions import ValidationError


def extract_token(request):
    try:
        source = request.headers.get('Authorization') or request.COOKIES.get('Authorization')
        return source.split('Bearer')[1].strip()
    except (IndexError, ValidationError, AttributeError):
        return None
