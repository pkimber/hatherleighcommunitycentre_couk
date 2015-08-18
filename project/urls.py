# -*- encoding: utf-8 -*-
from django.conf import settings
from django.conf.urls import (
    include,
    patterns,
    url,
)
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap

from block.models import Page


admin.autodiscover()


info_dict = {
  'queryset': Page.objects.pages(),
  'date_field': 'modified',
}

sitemaps = {
    'block': GenericSitemap(info_dict, priority=0.5, changefreq='monthly'),
}

urlpatterns = patterns(
    '',
    url(regex=r'^sitemap\.xml$',
        view='django.contrib.sitemaps.views.sitemap',
        kwargs={'sitemaps': sitemaps},
    ),
    url(regex=r'^',
        view=include('login.urls')
        ),
    url(regex=r'^admin/',
        view=include(admin.site.urls)
        ),
    url(regex=r'^block/',
        view=include('block.urls.block')
        ),
    url(regex=r'^compose/',
        view=include('compose.urls.compose')
        ),
    url(regex=r'^dash/',
        view=include('dash.urls')
        ),
    # this url include should come last
    url(regex=r'^',
        view=include('block.urls.cms')
        ),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   ^ helper function to return a URL pattern for serving files in debug mode.
# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user
