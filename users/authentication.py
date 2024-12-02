# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.exceptions import AuthenticationFailed as _, InvalidToken, AuthenticationFailed
# from rest_framework.status import HTTP_404_NOT_FOUND
# from users.models import WxUser
#
# # 自定义解析Token的方法
# from utils.token_get_user import get_wxuser_id
#
#
# class WXJWTAuthentication(JWTAuthentication):
#     def get_user(self, validated_data):
#         try:
#             user_id = get_wxuser_id(str(validated_data))
#         except KeyError:
#             raise InvalidToken(_('Token不包含可识别的用户标识'))
#
#         try:
#             user_id = WxUser.objects.get(pk=user_id)
#         except WxUser.DoesNotExist:
#             raise AuthenticationFailed(_('未找到用户'), code=HTTP_404_NOT_FOUND)