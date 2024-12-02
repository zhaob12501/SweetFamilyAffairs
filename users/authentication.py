# users/authentication.py

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User, Family


class WxAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 从请求头中获取自定义的认证信息
        print({k: v for k, v in request.META.items() if k.startswith('HTTP_X_WX_')})
        openid = request.META.get('HTTP_X_WX_OPENID')
        unionid = request.META.get('HTTP_X_WX_UNIDENTIFIER')
        if not openid:
            return None  # 没有提供openid，返回 None

        try:
            user = self.get_user_from_openid(openid, unionid)
        except IndexError:
            raise AuthenticationFailed('Invalid token format')
        except User.DoesNotExist:
            raise AuthenticationFailed('User not found')

        return (user, None)  # 返回用户和 None（无额外信息）

    def get_user_from_openid(self, openid, unionid):
        # 根据 openid 获取用户的逻辑
        try:
            return User.objects.get(openid=openid)
        except:
            # 假设你在某个地方需要创建家庭
            family_id = 1  # 你可以根据需要设置这个值
            family_name = '默认家庭'  # 默认家庭名称
            # 尝试获取或创建家庭
            family, family_created = Family.objects.get_or_create(
                id=family_id,
                defaults={'name': family_name}  # 设置默认名称
            )
            user = User.objects.create(username=f'用户{User.objects.count() + 10001}', openid=openid, unionid=unionid, family=family)
            user.set_password(user.username)
            return user
