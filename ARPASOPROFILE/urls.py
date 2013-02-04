from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login_url"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/list/'}, name="logout_url"),

    # forward control into local app
    url(r'^list/', include('PROFILE.urls')),
    url(r'^$', include('PROFILE.urls')),
    )
