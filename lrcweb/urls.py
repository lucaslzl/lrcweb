from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.views.static import serve

urlpatterns = []

#if settings.DEBUG:
urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT})]

urlpatterns += [
    path('admin/', admin.site.urls),
    path(r'', include('mainsite.urls')),
]
