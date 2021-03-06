
class Project(models.Model):
    LANGUAGE_TYPES = (
        ("Java", "Java"),
        ("PHP", "PHP"),
        ("Python", "Python"),
        ("C#", "C#"),
        ("Html", "Html"),
        ("Javascript", "Javascript"),
        ("C/C++", "C/C++"),
        ("Ruby", "Ruby"),
        ("Other", "Other"),
    )

    APP_TYPE = (
        ("Frontend", "Frontend"),
        ("Middleware", "Middleware"),
        ("Backend", "Backend"),
    )

    SERVER_TYPE = (
        ("Tomcat", "Tomcat"),
        ("Weblogic", "Weblogic"),
        ("JETTY", "JETTY"),
        ("Nginx", "Nginx"),
        ("Gunicorn", "Gunicorn"),
        ("Uwsgi", "Uwsgi"),
        ("Apache", "Apache"),
        ("IIS", "IIS"),
    )

    APP_ARCH = (
        ("Django", "Django"),
        ("Flask", "Flask"),
        ("Tornado", "Tornado"),
        ("Dubbo", "Dubbo"),
        ("SSH", "SSH"),
        ("Spring boot", "Spring boot"),
        ("Spring cloud", "Spring cloud"),
        ("Laravel", "Laravel"),
        ("ThinkPHP", "ThinkPHP"),
        ("Phalcon", "Phalcon"),
        ("other", "other"),
    )

    SOURCE_TYPE = (
        ("git", "git"),
        ("svn", "svn"),
    )

    name = models.CharField(verbose_name=u"项目名称", max_length=50, unique=True, null=False, blank=False)
    description = models.CharField(verbose_name=u"项目描述", max_length=255, null=True, blank=True)
    language_type = models.CharField(verbose_name=u"语言类型", choices=LANGUAGE_TYPES, max_length=30, null=True, blank=True)
    app_type = models.CharField(verbose_name=u"程序类型", choices=APP_TYPE, max_length=30, null=True, blank=True)
    server_type = models.CharField(verbose_name=u"服务器类型", choices=SERVER_TYPE, max_length=30, null=True, blank=True)
    app_arch = models.CharField(verbose_name=u"程序框架", choices=APP_ARCH, max_length=30, null=True, blank=True)
    source_type = models.CharField(max_length=255, choices=SOURCE_TYPE, verbose_name=u"源类型", blank=True)
    source_address = models.CharField(max_length=255, verbose_name=u"源地址", null=True, blank=True)
    appPath = models.CharField(verbose_name=u"程序部署路径", max_length=255, null=True, blank=True)
    configPath = models.CharField(verbose_name=u"配置文件路径", max_length=255, null=True, blank=True)
    product = models.ForeignKey(
            Product,
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            verbose_name=u"所属产品线"
    )
    owner = models.ForeignKey(
            AppOwner,
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            verbose_name=u"项目负责人"
    )
    serverList = models.ManyToManyField(
            Host,
            blank=True,
            verbose_name=u"所在服务器"
    )

    def __unicode__(self):
        return self.name
