from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_mysql.models import JSONField

from apps.keyboard import constants


class DataSet(models.Model):
    verbose_name = models.CharField(verbose_name=_("数据集别名"), max_length=128)
    dataset_name = models.CharField(verbose_name=_("数据集名称"), max_length=128)
    data_type = models.CharField(verbose_name=_("数据类型"), max_length=32, choices=constants.ProjectType.get_choices())
    description = models.CharField(verbose_name=_("数据集组合说明"), max_length=256)
    description_more = models.TextField(verbose_name=_("数据集具体描述"), null=True, blank=True)
    length = models.IntegerField(verbose_name=_("信号长度"))
    fs = models.IntegerField(verbose_name=_("采样频率"))

    # 基础字段
    created_at = models.DateTimeField(verbose_name=_("创建时间"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("更新时间"), blank=True, null=True, auto_now=True)

    class Meta:
        verbose_name = _("数据集")
        verbose_name_plural = _("数据集")
        ordering = ["id"]


class DataSetMfccFeature(models.Model):
    dataset_id = models.IntegerField(verbose_name=_("数据集ID"), db_index=True)
    label = models.CharField(verbose_name=_("数据标签"), db_index=True, max_length=32)
    mfcc_feature = JSONField(verbose_name=_("MFCC特征"), default=list)

    # 基础字段
    created_at = models.DateTimeField(verbose_name=_("创建时间"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("更新时间"), blank=True, null=True, auto_now=True)
