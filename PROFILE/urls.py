from django.conf.urls.defaults import *

urlpatterns = patterns('PROFILE.views',
#    url(r'^$', display_data, name='url_display_data'),
    url(r'^$', 'display_data', name='url_display_data'),
    )
