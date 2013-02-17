from django.conf.urls import patterns, url
from PROFILE.views import UserProfileList
from PROFILE.models import UserProfile

urlpatterns = patterns('',
    # view full list
    url(r'^$', UserProfileList.as_view(), name='url_display_data'), 

    # update record
    url(r'^(?P<slug>[\w\-]+)/edit/$', 'django.views.generic.create_update.update_object',
        {   'model': UserProfile, 
            'template_name': 'profile_CRU.html', 
            'login_required' : False, # no possibility to override /accounts/login redirection? 
            'post_save_redirect': "/" 
        }, 
        name="url_edit_profile"),
    )

# reference to plain variable (which is a CLASS) from views.py
#urlpatterns = patterns('PROFILE.views', url(r'$', 'display_data', name='url_display_data'),)
