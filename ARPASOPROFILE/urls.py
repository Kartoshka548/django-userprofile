from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'ARPASOPROFILE.views.home', name='home'),
    # url(r'^ARPASOPROFILE/', include('ARPASOPROFILE.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
