from threading import local

_user = local()

class RequestMiddleware:
    """Har bir so‘rovda foydalanuvchini saqlash"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _user.value = request.user
        response = self.get_response(request)
        return response

def get_current_user():
    """Joriy foydalanuvchini olish"""
    return getattr(_user, 'value', None)
