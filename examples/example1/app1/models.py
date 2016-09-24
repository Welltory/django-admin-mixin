# -*- coding: utf-8 -*-
from django.db import models


class SuperModel1(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    value1 = models.CharField(max_length=25)
    value2 = models.FloatField()


class SuperModel2(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    super_val1 = models.CharField(max_length=120)
    super_val2 = models.FloatField()
