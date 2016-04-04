django-taggit-jquery-tag-it
===========================

About
-----

This package adds the [Tag-it!](https://github.com/aehlke/tag-it) jquery GUI component to 
[django-taggit](https://github.com/alex/django-taggit), for autocompletion and a [nicer UI](http://aehlke.github.io/tag-it/examples.html). 

This is a Python 3/Django 1.8-compatible fork of [django-taggit-jquery-tag-it](https://github.com/rasca/django-taggit-jquery-tag-it), 
which is a fork of [django-taggit-autocomplete](https://github.com/Jaza/django-taggit-autocomplete), which is in turn a fork of
[django-tagging-autocomplete](http://code.google.com/p/django-tagging-autocomplete/). Python 2, Django <= 1.6 or [django-taggit-hvad](https://github.com/rasca/django-taggit-hvad)-compatibility have not been re-tested since forking.

Installation
------------

1. We recomend using `pip` and `virtualenv`:

```Bash
pip install git+https://github.com/technicaltitch/django-taggit-jquery-tag-it.git#egg=django_taggit_jquery_tag_it
```

2. Add `"django_taggit_jquery_tag_it"` to `INSTALLED_APPS` in your project's `settings.py` file:

```python
INSTALLED_APPS = (

    'taggit',
    'django_taggit_jquery_tag_it',

    # ...
```

3. Add the following line in your project `urls.py` file:

```python
url(r'^django_taggit_jquery_tag_it/', include('django_taggit_jquery_tag_it.urls')),
```

4. You should provide jQuery and jQuery UI (and a theme). If they aren't
   available in the current context, set `TAGGIT_AUTOCOMPLETE_CSS` and
   `TAGGIT_AUTOCOMPLETE_JS` in your settings file. Both settings must be lists.
   The theme must contain Core, Widget, Position, Autocomplete, and optionally
   Effects Core, Blind Effect and Highlight Effect, and can be generated at
   http://jqueryui.com/download/.

5. Enjoy

Usage
-----

Use our subclass of the `django-taggit` `taggit.managers.TaggableManager` class
in the tagged models.

Example:

```python
from django.db import models
from django_taggit_jquery_tag_it.managers import TaggableManager

class SomeModel(models.Model):
    tags = TaggableManager()
```
