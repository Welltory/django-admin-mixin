Exampe 2 for django_admin_mixin
===============================


Install
=======

```
# create db
python manage.py migrate

# load fixtures
python manage.py loaddata fixture_super_model1.json
python manage.py loaddata fixture_super_model2.json

# create super user
python manage.py createsuperuser
```

Description
===========

По-умолчанию, элементы из миксинов добавляются в конец.
Т.е.

Если в АдминМодель прописан параметр list_display:

```
list_display = ['field1', 'field2',]
```

То миксин

```
class ExampleMixinAdmin(admin.ModelAdmin):
    list_display = ['fieldN']
```

Добавил в `list_display` значение `fieldN` в конец:

```
list_display = ['field1', 'field2', 'fieldN']
```

Однако, в ряде случаев необходимо добавлять поля в начало списка. 
Например, вы делаете миксин UserMixinAdmin, который содержит основные поля для отображения информации о юзере: email, поиск по определенным полям
То может возникнуть желание показывать email юзера первым столбцом.
Чтобы это сделать, надо воспользоваться такой конструкией

```
class UserMixinAdmin(admin.ModelAdmin):
    list_display = ['email']
    list_display_to_start = True
```

Тогда в результате получим такой `list_display`:

```
list_display = ['email', 'field1', 'field2']
```

Для других полей это тоже справедливо. Добавля переменную `название_списка_to_start = True/False` вы можете регулировать куда должен миксин вставить свои элементы