from django.contrib.auth.models import Group, AbstractUser
from django.db import models


class Family(models.Model):
    name = models.TextField('家庭名称', blank=True, null=True, default='默认家庭')
    number = models.IntegerField("家庭成员数", blank=True, default=2)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user_fimaly'
        verbose_name = '家庭'
        verbose_name_plural = verbose_name


# Create your models here.
class User(AbstractUser):
    GENDER_TYPE = ((1, '女'),
                   (2, '男'))
    ROLE_TYPE = ((1, '物品策划者'),
                 (2, '积分追寻者'),
                 (3, '全能参与者'))
    openid = models.CharField('OpenId', unique=True, max_length=100, blank=True, null=True)
    username = models.CharField('用户名', max_length=20, unique=True, blank=True, null=True)
    role_type = models.IntegerField('角色', choices=ROLE_TYPE, default=1)

    tel = models.BigIntegerField('手机号', unique=True, blank=True, null=True)
    avatar_url = models.URLField('头像', help_text='头像', blank=True, null=True)
    unionid = models.CharField('UnionId', unique=True, max_length=100, blank=True, null=True)
    gender = models.IntegerField('性别', choices=GENDER_TYPE, default=1)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
