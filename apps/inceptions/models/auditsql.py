from django.db import models, IntegrityError
from django.utils.translation import ugettext_lazy as _

from common.mixins import NoDeleteModelMixin
import uuid
from users.models.user import User


PROCESS_CHOICE = (
    ('0', u'待批准'),
    ('1', u'未批准'),
    ('2', u'已批准'),
    ('3', u'处理中'),
    ('4', u'已完成'),
    ('5', u'已关闭')
)


OPTIONTYPE_CHOICE = (
    ('DDL', u'数据库定义语言'),
    ('DML', u'数据库操纵语言')
)


class AuditContent(NoDeleteModelMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=100, verbose_name=u'标题')
    operate_type = models.CharField(max_length=5, default='DML', choices=OPTIONTYPE_CHOICE,
                                    verbose_name=u'操作类型: DDL or DML')
    proposer = models.CharField(max_length=30, default='', verbose_name=u'申请人， 一般为开发或者产品，存储username')
    verifier = models.CharField(max_length=30, default='', verbose_name=u'批准人，一般为项目经理或Leader， 存储username')
    operator = models.CharField(max_length=30, default='', verbose_name=u'执行人，一般为DBA， 存储username')
    email_cc = models.CharField(max_length=1024, default='', verbose_name=u'抄送人， 存储contact_id，以逗号分隔')
    host = models.ForeignKey("DbHost", null=False, default='', max_length=30, verbose_name=u'操作数据库主机')
    database = models.CharField(null=False, default='', max_length=80, verbose_name=u'操作数据库')
    progress = models.CharField(max_length=10, default='0', choices=PROCESS_CHOICE, verbose_name=u'任务进度')
    verifier_time = models.DateTimeField(auto_now_add=True, verbose_name=u'审批时间')
    operate_time = models.DateTimeField(auto_now_add=True, verbose_name=u'执行的时间')
    close_user = models.CharField(max_length=30, default='', verbose_name=u'关闭记录的用户')
    close_reason = models.CharField(max_length=1024, default='', verbose_name=u'关闭原因')
    close_time = models.DateTimeField(auto_now_add=True, verbose_name=u'关闭时间')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    def __str__(self):
        return self.title

    def proposer_avatar_file(self):
        return User.objects.get(username=self.proposer).avatar_file

    def email_cc_list(self):
        return '\n'.join(
            Contact.objects.filter(contact_id__in=self.email_cc.split(',')).values_list('contact_email', flat=True))

    class Meta:
        verbose_name = u'审核内容'
        verbose_name_plural = verbose_name

        db_table = 'incetpion_audit'
        unique_together = ('title',)


class AuditDetail(NoDeleteModelMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    ol = models.ForeignKey(AuditContent, on_delete=models.CASCADE, verbose_name=u'关联审核内容表id')
    contents = models.TextField(default='', verbose_name=u'提交的内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    class Meta:
        verbose_name = u'线上审核内容详情表'
        verbose_name_plural = verbose_name

        db_table = 'inception_audit_detail'


export_progress_choices = (
    ('0', u'未执行'),
    ('1', u'导出中'),
    ('2', u'已生成')
)


class AuditContentsReply(NoDeleteModelMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    reply = models.ForeignKey(AuditContent, on_delete=models.CASCADE, null=False, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default='')
    reply_contents = models.TextField(default='', verbose_name=u'回复内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'回复时间')

    class Meta:
        verbose_name = u'线上审核回复表'
        verbose_name_plural = verbose_name

        default_permissions = ()
        db_table = 'inception_audit_reply'

    def reply_id(self):
        return self.reply.id

    def user_id(self):
        return self.user.uid

exec_progress = (
    ('0', u'未执行'),
    ('1', u'已完成'),
    ('2', u'处理中'),
    ('3', u'回滚中'),
    ('4', u'已回滚'),
)


class IncepExecTask(NoDeleteModelMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    uid = models.IntegerField(null=False, default=0, verbose_name=u'操作用户uid')
    user = models.CharField(max_length=30, null=False, verbose_name=u'操作用户')
    taskid = models.CharField(null=False, max_length=128, verbose_name=u'任务号')
    related_id = models.UUIDField(null=False, default=0, verbose_name=u'关联AuditContent的主键id')
    category = models.CharField(null=False, max_length=2, default='0', choices=(('0', u'线下任务'), ('1', u'线上任务')),
                                verbose_name=u'任务分类')
    dst_host = models.CharField(null=False, max_length=30, verbose_name=u'操作目标数据库主机')
    dst_database = models.CharField(null=False, max_length=80, verbose_name=u'操作目标数据库')
    sql_content = models.TextField(verbose_name=u'执行的SQL', default='')
    type = models.CharField(max_length=5, default='', choices=(('DDL', u'数据库定义语言'), ('DML', u'数据库操纵语言')))
    sqlsha1 = models.CharField(null=False, max_length=120, default='', verbose_name=u'sqlsha1')
    rollback_sqlsha1 = models.CharField(null=False, max_length=120, default='', verbose_name=u'rollback sqlsha1')
    celery_task_id = models.CharField(null=False, max_length=256, default='', verbose_name=u'celery执行任务ID')
    exec_status = models.CharField(max_length=10, default='0', choices=exec_progress, verbose_name=u'执行进度')
    sequence = models.CharField(null=False, default='', max_length=1024, verbose_name=u'备份记录id，inception生成的sequence')
    affected_row = models.IntegerField(null=False, default=0, verbose_name=u'预计影响行数')
    backup_dbname = models.CharField(null=False, max_length=1024, default='', verbose_name=u'inception生成的备份的库名')
    exec_log = models.TextField(verbose_name=u'执行成功的记录', default='')
    make_time = models.DateTimeField(auto_now_add=True, verbose_name=u'生成时间')

    class Meta:
        verbose_name = u'生成Inception执行任务'
        verbose_name_plural = verbose_name

        default_permissions = ()
        db_table = 'inception_task'


class Contact(NoDeleteModelMixin):
    """联系人表"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    contact_name = models.CharField(max_length=30, default='', verbose_name=u'联系人姓名')
    contact_email = models.EmailField(max_length=128, default='', verbose_name=u'联系人邮箱')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')

    def __str__(self):
        return self.contact_name

    class Meta:
        verbose_name = u'联系人'
        verbose_name_plural = verbose_name

        default_permissions = ()
        db_table = 'inception_contact'

        unique_together = ('contact_name', 'contact_email')

