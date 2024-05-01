import jwt
from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission

class IsAuthenticatedJWT(BasePermission):
    def has_permission(self, request, view):
        token = request.COOKIES.get('jwt')
        if not token:
            token = request.headers.get('Authorization')
        if token:
            try:
                payload = jwt.decode(token, 'HeMaNt', algorithms=['HS256'], options={"verify_signature": True})
                user = User.objects.get(id=payload['user_id'])
                if user:
                    return True
            except:
                return False
            else:
                return False
        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
