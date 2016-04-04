from django.conf.urls import *
from django.contrib.admin.views.decorators import staff_member_required

from .views import list_tags

urlpatterns = [url(r'^list/$', staff_member_required(list_tags), name='django_taggit_jquery_tag_it-list'),]
