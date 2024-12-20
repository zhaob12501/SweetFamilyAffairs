from django.http import JsonResponse
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Family
from users.serializers import UserSerializer, FamilySerializer

User = get_user_model()

class FimalyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Family.objects.all()
    serializer_class = FamilySerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WxAuthView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        openid = request.META.get('HTTP_X_WX_OPENID')
        user = User.objects.get(openid=openid)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data)
