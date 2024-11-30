from social_django.signals import user_social_auth
from django.dispatch import receiver

@receiver(user_social_auth)
def social_auth_user_details(request, user, sociallogin):
    """社交登录后保存用户信息"""
    user.weixin_openid = sociallogin.uid
    user.save()