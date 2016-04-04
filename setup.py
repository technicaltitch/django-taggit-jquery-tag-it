# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
 
long_description = open('README.md').read()
 
setup(
    name='django-taggit-jquery-tag-it',
    version='0.1',
    description='Autocompletion for django-taggit',
    long_description=long_description,
    author=u'Chris Preager',
    author_email='cpreager@hotmail.com',
    url='https://github.com/technicaltitch/django-taggit-jquery-tag-it.git',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[
        'Django>=1.8',
        'django-taggit',
    ],
    include_package_data=True,
    zip_safe=False,
) 
