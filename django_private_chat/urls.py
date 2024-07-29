# -*- coding: utf-8 -*-
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(
        route=r'^dialogs/(?P<username>[\w.@+-]+)$',
        view=views.DialogListView.as_view(),
        name='dialogs_detail'
    ),
    re_path(
        route=r'^dialogs/$',
        view=views.DialogListView.as_view(),
        name='dialogs'
    ),
]
