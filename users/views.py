from django.http import JsonResponse
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.views import APIView

from users.serializers import WxUserSerializer

User = get_user_model()

class WxUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = WxUserSerializer


class WxUserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        headers = request.META
        return JsonResponse(
            headers
        )