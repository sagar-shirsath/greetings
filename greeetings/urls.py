
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    url(r'^', include('webapp.urls', namespace='homepage')),

]
