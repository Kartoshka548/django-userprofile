from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),


    # forward control into local app
#    url(r'^list/', 'PROFILE.views.display_data', name='url_display_data'),



    # forward control into local app
    url(r'^list/', include('PROFILE.urls')),
    )
