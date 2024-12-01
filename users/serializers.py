from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from users.models import WxUser


class WxTokenObtainSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['openid'] = user.openid
        return token

    def validate(self, attrs):
        old_data = super().validate(attrs)
        data = {
            "code": 100,
            "msg": "登录成功",
            "openid": self.user.openid,
            "refresh": old_data['refresh'],
            "access": old_data['access'],
        }
        return data


class WxUserSerializer(serializers.ModelSerializer):
    """ 用户序列化器 """
    openid = serializers.CharField(source='openid', read_only=True)

    class Meta:
        model = WxUser
        fields = '__all__'

    def validate(self, data):
        openid = data.get('openid')
        if openid:
            refresh = WxTokenObtainSerializer.get_token(openid)
            data = {
                "code": 100,
                "msg": "登录成功",
                "openid": self.user.openid,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return data
        return ValidationError("OpenId未传")

    def is_valid(self, raise_exception=None):
        if not super().is_valid(raise_exception):
            self._errors.update({"code": 101, "message": "OpenId有误"})
        return not bool(self._errors)

class WxUserInfoSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
