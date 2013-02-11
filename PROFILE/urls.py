from django.conf.urls import patterns, url
from PROFILE.views import UserProfileList

urlpatterns = patterns('',
    url(r'$', UserProfileList.as_view(), name='url_display_data'),)

# reference to plain variable (which is a CLASS) from views.py
#urlpatterns = patterns('PROFILE.views', url(r'$', 'display_data', name='url_display_data'),)
