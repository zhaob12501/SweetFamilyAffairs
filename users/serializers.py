from rest_framework import serializers
from users.models import User, Family


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """ 用户序列化器 """

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'username', 'family', 'gender', 'role_type', 'tel']
