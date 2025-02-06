from threading import local

_user = local()  # Har bir request uchun user ni saqlash

class RequestUserMiddleware:
    """Har bir so‘rovda foydalanuvchini saqlash"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _user.value = request.user  # So‘rovga tegishli user ni saqlash
        response = self.get_response(request)
        return response
