from django.db import models, IntegrityError
from django.utils.translation import ugettext_lazy as _

from common.mixins import NoDeleteModelMixin
import uuid
from assets.models import Asset

class Inception(NoDeleteModelMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.CharField(max_length=30, null=False, verbose_name=u'用户名')
    password = models.CharField(max_length=128, null=False, verbose_name=u'密码')
    host = models.CharField(max_length=32, null=False, verbose_name=u'ip地址')
    port = models.IntegerField(null=False, verbose_name=u'端口')
    type = models.IntegerField(null=False, default=0, verbose_name=u'0:线下数据库，1:线上数据库')
    purpose = models.CharField(default='0', max_length=2, choices=(('0', u'审核'), ('1', u'查询')), verbose_name=u'用途')
    is_active = models.IntegerField(null=False, default=1, verbose_name=u'1:启用，2：禁用')
    protection_user = models.TextField(default='root', null=False, verbose_name=u'被保护的数据库账号， 以逗号分隔')
    backup_asset = models.ForeignKey('Asset', on_delete=models.CASCADE, verbose_name="ssh machive")
    backup_user = models.CharField(max_length=32, verbose_name="incetion backup user")
    backup_password = models.CharField(max_length=64, verbose_name="inception backup password")
    comment = models.CharField(max_length=128, verbose_name=u'主机描述')



    class Meta:
        verbose_name = u'inception数据库账号'
        verbose_name_plural = verbose_name

        unique_together = [('host', 'port', 'is_active')]

        default_permissions = ()
        db_table = 'inception_hostinfo'