from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', name="login_url"), # renders registration/login.html template by default
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout_url"), # next_page is where it redirects
    url(r'^new/$', 'PROFILE.views.create_new_user', name="create_new_user"),

    # forward control into local app
    url(r'^', include('PROFILE.urls')),
    )
