from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from hello.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
]
