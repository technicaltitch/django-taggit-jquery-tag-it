from django import forms
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

from taggit.utils import edit_string_for_tags
from . import settings


class TagAutocomplete(forms.TextInput):
    input_type = 'text'

    def render(self, name, value, attrs=None):
        if value is not None and not isinstance(value, str):
            value = edit_string_for_tags(
                    [o.tag for o in value.select_related("tag")])
        html = super(TagAutocomplete, self).render(name, value, attrs)

        js = u"""
            <script type="text/javascript">
                (function($) {
                    $(document).ready(function() {
                        $("#%(id)s").tagit({
                            caseSensitive: false,
                            autocomplete: {delay: 0, minLength: 1, source: function(search, showChoices) {
                                options = this;
                                $.getJSON("%(source)s", {
                                    term: search.term.toLowerCase()
                                }, function(data) {
                                    showChoices(options._subtractArray(data, options.assignedTags()));
                                });
                            }},
                        });
                    });
                })(jQuery);
            </script>
            """ % ({
                'id': attrs['id'],
                'source': reverse('django_taggit_jquery_tag_it-list')
            })
        return mark_safe("\n".join([html, js]))

    class Media:
        css = {
            'all': settings.CSS,
        }
        js = settings.JS
        
