#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
from django.db import models, IntegrityError
from django.utils.translation import ugettext_lazy as _

from common.mixins import NoDeleteModelMixin
import uuid
import random

ASSET_STATUS = (
    (str(1), u"使用中"),
    (str(2), u"未使用"),
    (str(3), u"故障"),
    (str(4), u"其它"),
)

ASSET_TYPE = (
    (str(1), u"物理机"),
    (str(2), u"虚拟机"),
    (str(3), u"容器"),
    (str(4), u"网络设备"),
    (str(5), u"安全设备"),
    (str(6), u"其他")
)

ASSET_VENDOR_CHOICE = (
    ("ibm", "ibm"),
    ("dell", "dell")
)

ASSET_EVN_CHOICE = (
    ("test", "test"),
    ("dev", "dev"),
    ("product", "product")
)


ASSET_SSH_PORT =(
    (22, 22),
    (2222, 2222),
    (222, 222)
)


class UserInfo(NoDeleteModelMixin):
    username = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=64, null=True)

    def __unicode__(self):
        return self.username


class Idc(NoDeleteModelMixin):
    name = models.CharField(u"机房名称", max_length=255, unique=True)
    address = models.CharField(u"机房地址", max_length=100, blank=True)
    tel = models.CharField(u"机房电话", max_length=30, blank=True)
    contact = models.CharField(u"客户经理", max_length=30, blank=True)
    contact_phone = models.CharField(u"移动电话", max_length=30, blank=True)
    jigui = models.CharField(u"机柜信息", max_length=30, blank=True)
    ip_range = models.CharField(u"IP范围", max_length=30, blank=True)
    bandwidth = models.CharField(u"接入带宽", max_length=30, blank=True)
    instance_id = models.CharField(max_length=64, verbose_name='实例ID', null=True, blank=True)
    memo = models.TextField(u"备注信息", max_length=200, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'数据中心'
        verbose_name_plural = verbose_name
        db_table = 'cmdb_idc'


class Cabinet(NoDeleteModelMixin):
    idc = models.ForeignKey(Idc, verbose_name=u"所在机房", on_delete=models.SET_NULL, null=True, blank=True)
    cabient_code = models.CharField(u"机架标识", max_length=255, unique=True)
    cabient_name = models.CharField(u"机架名称", max_length=100)
    remark = models.CharField(u"描述", max_length=100, blank=True)

    assets = models.ManyToManyField(
        'Asset',
        blank=True,
        verbose_name=u"所在服务器", db_table='cmdb_asset_cabinet'
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'数据中心机架'
        verbose_name_plural = verbose_name
        db_table = 'cmdb_cabinet'


class Asset(NoDeleteModelMixin):
    hostname = models.CharField(max_length=50, verbose_name=u"主机名", unique=True)
    manager_ip = models.GenericIPAddressField(u"管理IP", max_length=15)
    idc = models.ForeignKey(Idc, verbose_name=u"所在机房", on_delete=models.SET_NULL, null=True, blank=True)
    wlan_ip = models.CharField(u"其它IP", max_length=100, blank=True)
    asset_type = models.CharField(u"设备类型", choices=ASSET_TYPE, max_length=30, null=True, blank=True)
    status = models.CharField(u"设备状态", choices=ASSET_STATUS, max_length=30, null=True, blank=True)
    env = models.CharField( u"环境",max_length=16, choices=ASSET_EVN_CHOICE, blank=False, null=False, default='dev')
    port = models.IntegerField(verbose_name="登录端口", default='22', choices=ASSET_SSH_PORT, null=False, blank=False)
    adminuser = models.ForeignKey(verbose_name="登录用户", to='AssetAdminUser',
                                  on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(verbose_name='资产项目', to='AssetCategory', on_delete=models.CASCADE, )
    business = models.ForeignKey(verbose_name='资产业务', to='AssetBusiness', on_delete=models.SET_NULL, null=True,
                                 blank=True)
    def __unicode__(self):
        return self.hostname

    class Meta:
        verbose_name = u'资产'
        verbose_name_plural = verbose_name
        db_table = 'cmdb_asset'


class AssetInfo(NoDeleteModelMixin):
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE, primary_key=True)
    asset_no = models.CharField(u"资产编号", max_length=50, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="")
    os = models.CharField(u"操作系统", max_length=100, blank=True)
    vendor = models.CharField(u"设备厂商", choices=ASSET_VENDOR_CHOICE, max_length=8, blank=True)
    buy_time = models.CharField(u"时间", max_length=50, blank=True)
    cpu_model = models.CharField(u"CPU型号", max_length=100, blank=True)
    cpu_num = models.CharField(u"CPU数量", max_length=100, blank=True)
    memory = models.CharField(u"内存大小", max_length=30, blank=True)
    disk = models.CharField(u"硬盘信息", max_length=255, blank=True)
    sn = models.CharField(u"SN号 码", max_length=60, blank=True)
    position = models.CharField(u"所在位置", max_length=100, blank=True)
    remark = models.TextField(u"备注信息", max_length=200, blank=True)

    def __unicode__(self):
        return self.asset_no

    class Meta:
        verbose_name = u'资产'
        verbose_name_plural = verbose_name
        db_table = 'cmdb_assetinfo'


class AssetGroup(NoDeleteModelMixin):
    name = models.CharField(u"服务器组名", max_length=30, unique=True)
    remark = models.CharField(u"描述", max_length=100, blank=True)
    assets = models.ManyToManyField(
        Asset,
        blank=True,
        verbose_name=u"所在服务器",
        db_table='cmdb_asset_group'
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'资产组'
        verbose_name_plural = verbose_name
        db_table = 'cmdb_group'


class AssetAdminUser(models.Model):
    hostname = models.CharField(max_length=64, verbose_name='名称', unique=True)
    username = models.CharField(max_length=64, verbose_name="用户名", default='root', null=True, blank=True)
    password = models.CharField(max_length=256, blank=True, null=True, verbose_name='密码')
    private_key = models.FileField(upload_to='upload/privatekey/%Y%m%d{}'.format(random.randint(0, 99999)),
                                   verbose_name="私钥", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间', blank=True)
    updaet_time = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间', blank=True)

    class Meta:
        db_table = "cmdb_adminuser"
        verbose_name = "资产用户"
        verbose_name_plural = '资产用户'

    def __str__(self):
        return self.hostname


class AssetCategory(models.Model):
    projects = models.CharField(max_length=128, verbose_name='资产项目')
    remark = models.CharField(max_length=255, verbose_name="备注", null=True, blank=True)

    class Meta:
        db_table = "cmdb_category"
        verbose_name = "资产项目"
        verbose_name_plural = '资产项目'

    def __str__(self):
        return self.projects


class AssetBusiness(models.Model):
    business_name = models.CharField(max_length=128, verbose_name='业务')
    remark = models.CharField(max_length=255, verbose_name="备注", null=True, blank=True)

    class Meta:
        db_table = "cmdb_business"
        verbose_name = "资产业务"
        verbose_name_plural = '资产业务'

    def __str__(self):
        return self.business_name
