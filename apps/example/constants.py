# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _


class MathOp:
    MUL = "mul"
    ADD = "add"


OP_CHOICES = ((MathOp.ADD, _("加法")), (MathOp.MUL, _("乘法")))
