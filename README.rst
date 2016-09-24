===============================
django admin mixin
===============================


.. image:: https://img.shields.io/pypi/v/django_admin_mixin.svg
        :target: https://pypi.python.org/pypi/django_admin_mixin

.. image:: https://img.shields.io/travis/WarmongeR1/django_admin_mixin.svg
        :target: https://travis-ci.org/WarmongeR1/django_admin_mixin

.. image:: https://readthedocs.org/projects/django-admin-mixin/badge/?version=latest
        :target: https://django-admin-mixin.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/WarmongeR1/django_admin_mixin/shield.svg
     :target: https://pyup.io/repos/github/WarmongeR1/django_admin_mixin/
     :alt: Updates


Модуль реализует механизм примесей (mixin) для Django admin.
С помощью модуля можно упростить конфигурацию admin.py

Применение:

Если у вас есть много моделей, которые имеют повторяющиеся поля.
С этими полями как-то надо работать в админке, например, фильтровать, искать по ним.
То вы можете вынести этот повторяющийся блок в mixin.

* Free software: MIT license
* Documentation: https://django-admin-mixin.readthedocs.io.


Install
-------

`pip install django-admin-mixin`

Configuration
-------------



Usage
-----

Example models::

    # models.py

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

Example admin.py::

    # admin.py
    from django.contrib import admin
    from super_app.models import SuperModel1, SuperModel2
    from django_admin_mixin import MixinAdminCombiner

    class TimeMixinAdmin(admin.ModelAdmin):
        list_display = ['created_at']
        ordering = ['-created_at']
        list_filter = ['created_at', 'updated_at']

    @admin.register(SuperModel1)
    class SuperModel1Admin(MixinAdminCombiner):
        mixins = [TimeMixinAdmin, ]
        list_display = ['value1']


    @admin.register(SuperModel2)
    class SuperModel2Admin(MixinAdminCombiner):
        mixins = [TimeMixinAdmin, ]
        list_display = ['super_val1', 'super_val2']

Result:

<image>

Features
--------

* TODO
