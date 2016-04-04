from django.conf import settings

# Both settings must be lists or tuples of URLs
CSS = getattr(settings, 'TAGGIT_AUTOCOMPLETE_CSS', ())
CSS = CSS + ('django_taggit_jquery_tag_it/css/jquery.tagit.css', )
JS = getattr(settings, 'TAGGIT_AUTOCOMPLETE_JS', ())
JS = JS + ('django_taggit_jquery_tag_it/js/tag-it.js', )
