# -*- encoding: utf-8 -*-
from django.conf import settings
from django.conf.urls import (
    include,
    patterns,
    url,
)
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(regex=r'^',
        view=include('login.urls')
        ),
    url(regex=r'^admin/',
        view=include(admin.site.urls)
        ),
    url(regex=r'^cms/',
        view=include('cms.urls.cms')
        ),
    url(regex=r'^compose/',
        view=include('compose.urls')
        ),
    url(regex=r'^dash/',
        view=include('dash.urls')
        ),
    # this url include should come last
    url(regex=r'^',
        view=include('cms.urls.page')
        ),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   ^ helper function to return a URL pattern for serving files in debug mode.
# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user
