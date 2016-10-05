# -*- coding: utf-8 -*-

from django.contrib import admin

__all__ = [
    'MixinAdminCombiner',
]


class MixinAdminCombiner(admin.ModelAdmin):
    list_per_page = 25
    show_full_result_count = False

    def _process_list(self, func):
        list_name = str(func.__name__[4:])
        result = getattr(self, list_name, [])
        if isinstance(result, bool):
            result = []
        setattr(self, list_name, result)

        for mixin in self.get_mixins():
            mixin_list = getattr(mixin, list_name, [])
            if mixin_list is None or not isinstance(mixin_list, (tuple, list)):
                continue
            result = self.add(
                getattr(self, list_name, []),
                mixin_list,
                mixin,
                to_start=getattr(mixin,
                                 '{}_to_start'.format(list_name), False)
            )
            setattr(self, list_name, result)
        return result

    def get_mixins(self):
        return getattr(self, 'mixins', [])

    def get_list_display(self, request):
        if '__str__' in self.list_display:
            self.list_display = list(self.list_display)
            self.list_display.remove('__str__')

        return self._process_list(self.get_list_display)

    def get_ordering(self, request):
        return self._process_list(self.get_ordering) or ()

    def get_list_filter(self, request):
        return self._process_list(self.get_list_filter)

    # def get_list_select_related(self, request):
    #     return self._process_list(self.get_list_select_related)

    def get_readonly_fields(self, request, obj=None):
        return self._process_list(self.get_readonly_fields)

    def get_prepopulated_fields(self, request, obj=None):
        return self._process_list(self.get_prepopulated_fields)

    def get_search_fields(self, request):
        return self._process_list(self.get_search_fields)

    def has_attr(self, attr):
        if not hasattr(self, 'model'):
            return True
        for field in self.model._meta.fields:
            if field.attname == attr:
                return True
        return False

    def gen_field_list(self, model, keys):
        result = []
        for field in model._meta.fields:
            for key in keys:
                if field.attname == key:
                    result.append(key)
        return result

    def _add(self, items, item, to_start):
        if to_start:
            items.insert(0, item)
        else:
            items.append(item)

    def add(self, admin_list, keys, mixin, **options):
        if isinstance(admin_list, tuple):
            admin_list = list(admin_list)
        if admin_list is None:
            admin_list = []
        for key in keys:
            if key in admin_list:
                continue

            if isinstance(key, str):
                if '__' in key or key.startswith('-'):
                    self._add(admin_list, key, options.get('to_start', False))
                elif self.has_attr(key) or key == 'user' or hasattr(mixin, key):
                    self._add(admin_list, key, options.get('to_start', False))
            else:
                self._add(admin_list, key, options.get('to_start', False))

        return admin_list
