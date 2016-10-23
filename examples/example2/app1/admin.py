# -*- coding: utf-8 -*-
from app1.models import SuperModel1, SuperModel2
from django.contrib import admin
from django_admin_mixin import MixinAdminCombiner


class TimeMixinAdmin(admin.ModelAdmin):
    list_display = ['created_at']
    list_display_to_start = True

    list_filter = ['created_at', 'updated_at']
    list_filter_to_start = True

    ordering = ['-created_at']


@admin.register(SuperModel1)
class SuperModel1Admin(MixinAdminCombiner):
    mixins = [TimeMixinAdmin, ]
    list_display = ['value1']


@admin.register(SuperModel2)
class SuperModel2Admin(MixinAdminCombiner):
    mixins = [TimeMixinAdmin, ]
    list_display = ['super_val1', 'super_val2']
