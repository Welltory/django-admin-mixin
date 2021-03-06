#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [i.strip() for i in open("requirements.txt").readlines()]

test_requirements = [i.strip() for i in
                     open("requirements_test.txt").readlines()]

setup(
    name='django-admin-mixin',
    version='0.1.2',
    description="Модуль реализует механизм примесей (mixin) для Django admin.",
    long_description=readme + '\n\n' + history,
    author="Alexander Sapronov",
    author_email='sapronov.alexander92@gmail.com',
    url='https://github.com/WarmongeR1/django_admin_mixin',
    packages=[
        'django_admin_mixin',
    ],
    package_dir={
        'django_admin_mixin': 'django_admin_mixin'
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='django_admin_mixin',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
