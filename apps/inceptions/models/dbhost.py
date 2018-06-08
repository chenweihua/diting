from django.db import models, IntegrityError
from django.utils.translation import ugettext_lazy as _

from common.mixins import NoDeleteModelMixin
import uuid

class DbHost(NoDeleteModelMixin):
    '''
    数据库连接信息表
    '''
    ROOM_CHOICE=(("aliyun","aliyun"),("dev","dev"))
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    connection_name = models.CharField(max_length=50,verbose_name=_('Connect name')) #连接名
    computer_room = models.CharField(max_length=50,choices=ROOM_CHOICE, verbose_name=_('Computer room')) #机房
    db_host = models.CharField(max_length=100, verbose_name=_('Db host ip address')) #ip地址
    username = models.CharField(max_length=150, verbose_name=_('Db user')) #数据库用户名
    port = models.IntegerField(verbose_name=_('Db port')) #端口
    password = models.CharField(max_length=50,verbose_name=_('Db password')) #数据库密码
    before = models.TextField(null=True, verbose_name=_('Before Context')) #提交工单 钉钉webhook发送内容
    after = models.TextField(null=True, verbose_name=_('After Context'))  #工单执行成功后 钉钉webhook发送内容
    url = models.TextField(blank=True, verbose_name=_('DingDing url'))    #钉钉webhook url地址

    class Meta:
        verbose_name = u'inception数据库'
        verbose_name_plural = verbose_name

        unique_together = [('connection_name')]

        default_permissions = ()
        db_table = 'inception_dbinfo'