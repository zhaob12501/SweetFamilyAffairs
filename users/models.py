from django.contrib.auth.models import Group, AbstractUser
from django.db import models


class WxFimalyGroup(Group):
    description = models.TextField(blank=True, null=True, verbose_name='家庭')

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'wxuser_fimaly'
        verbose_name = '微信用户家庭'
        verbose_name_plural = verbose_name

# Create your models here.
class WxUser(AbstractUser):
    GENDER_TYPE = ((1, '女生'),
                   (2, '男生'))
    openid = models.CharField('OpenId', unique=True, max_length=100, blank=True, null=True)
    username = models.CharField('用户名', max_length=20, unique=True, blank=True, null=True)
    tel = models.BigIntegerField('手机号', unique=True, blank=True, null=True)
    avatar_url = models.URLField('头像', help_text='头像', blank=True, null=True)
    unionid = models.CharField('UnionId', unique=True, max_length=100, blank=True, null=True)
    gender = models.IntegerField('性别', choices=GENDER_TYPE, default=1)
    family = models.ForeignKey(WxFimalyGroup, on_delete=models.CASCADE, default=None)

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.openid

    class Meta:
        db_table = 'wxuser'
        verbose_name = '微信用户'
        verbose_name_plural = verbose_name
