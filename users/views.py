import requests
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import WxUser


class WeChatLoginView(APIView):
    def post(self, request):
        code = request.data.get('code')
        appid = 'wx2957e3a81d403bf6'
        secret = '498861b83ae925efdfcd1cfc0d603afe'

        # 请求微信 API 获取 openid 和 session_key
        url = f'https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code'
        response = requests.get(url)
        data = response.json()

        if 'errcode' in data:
            return Response({'error': data['errmsg']}, status=status.HTTP_400_BAD_REQUEST)

        openid = data['openid']
        session_key = data['session_key']

        # 查找或创建用户
        user, created = WxUser.objects.get_or_create(wechat_openid=openid)

        # 生成 JWT token
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
