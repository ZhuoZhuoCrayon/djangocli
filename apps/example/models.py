from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Book(models.Model):
    class PackageType:
        PAPERBACK = 1
        HARDBACK = 2

    PACKAGE_TYPE_CHOICES = (
        (PackageType.PAPERBACK, _("平装")),
        (PackageType.HARDBACK, _("精装")),
    )

    # 属性
    name = models.CharField(verbose_name=_("书名"), max_length=128)
    ISBN = models.CharField(verbose_name=_("ISBN"), max_length=64)
    publication_date = models.DateField(verbose_name=_("出版日期"))
    package_type = models.IntegerField(verbose_name=_("包装类型"), choices=PACKAGE_TYPE_CHOICES)

    # 关联
    publisher_id = models.IntegerField(verbose_name=_("出版社ID"))
    author_ids = models.JSONField(verbose_name=_("作者ID列表"), default=list)

    # 基础字段
    created_at = models.DateTimeField(verbose_name=_("创建时间"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("更新时间"), blank=True, null=True, auto_now=True)

    class Meta:
        verbose_name = _("书籍")
        verbose_name_plural = _("书籍")
        ordering = ["id"]


class Publisher(models.Model):
    name = models.CharField(verbose_name=_("出版社名称"), max_length=128)
    address = models.CharField(verbose_name=_("出版社地址"), max_length=128)
    city = models.CharField(verbose_name=_("所在城市"), max_length=64)
    country = models.CharField(verbose_name=_("所在国家"), max_length=64)
    website = models.URLField(null=True, blank=True)

    # 基础字段
    created_at = models.DateTimeField(verbose_name=_("创建时间"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("更新时间"), blank=True, null=True, auto_now=True)

    class Meta:
        verbose_name = _("出版社")
        verbose_name_plural = _("出版社")
        ordering = ["id"]


class Author(models.Model):
    first_name = models.CharField(verbose_name=_("名"), max_length=36)
    last_name = models.CharField(verbose_name=_("姓氏"), max_length=64)
    birthday = models.DateField(verbose_name=_("出生日期"), null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # 基础字段
    created_at = models.DateTimeField(verbose_name=_("创建时间"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("更新时间"), blank=True, null=True, auto_now=True)

    class Meta:
        verbose_name = _("作者")
        verbose_name_plural = _("作者")
        ordering = ["id"]
