from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import HouseholdTask, TaskCompletion, RedeemItem, PointsHistory, PointsRedeem
from .serializers import HouseholdTaskSerializer, TaskCompletionSerializer, RedeemItemSerializer, PointsHistorySerializer, PointsRedeemSerializer


class ApiView(APIView):
    def get(self,request):
        return Response({}, status=status.HTTP_200_OK)

class TokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # 可以在这里添加额外的用户信息到响应中
        return Response({
            'access': response.data['access'],
            'refresh': response.data['refresh'],
            'user': {
                'username': request.user.username,
                'email': request.user.email,
            }
        })


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected view!'})


class HouseholdTaskViewSet(viewsets.ModelViewSet):
    """
    家务任务视图集
    """
    queryset = HouseholdTask.objects.all()
    serializer_class = HouseholdTaskSerializer


class TaskCompletionViewSet(viewsets.ModelViewSet):
    """
    任务完成记录视图集
    """
    queryset = TaskCompletion.objects.all()
    serializer_class = TaskCompletionSerializer


class RedeemItemViewSet(viewsets.ModelViewSet):
    """
    兑换物品视图集
    """
    queryset = RedeemItem.objects.all()
    serializer_class = RedeemItemSerializer


class PointsHistoryViewSet(viewsets.ModelViewSet):
    """
    积分历史视图集
    """
    queryset = PointsHistory.objects.all()
    serializer_class = PointsHistorySerializer


class PointsRedeemViewSet(viewsets.ModelViewSet):
    """
    积分兑换视图集
    """
    queryset = PointsRedeem.objects.all()
    serializer_class = PointsRedeemSerializer
