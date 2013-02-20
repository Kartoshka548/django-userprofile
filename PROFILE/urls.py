from django.conf.urls import patterns, url
from PROFILE.views import UserProfileList, UserProfileUpdate, UserProfileCreate, UserProfileReview
from PROFILE.models import UserProfile

urlpatterns = patterns('',
    # view full list
    url(r'^$', UserProfileList.as_view(), name='url_display_data'), 

    # create record
    url(r'^create(/)?$', UserProfileCreate.as_view(), name="url_create_profile"),

    # update record
    url(r'^(?P<slug>[\w\-]+)/edit(/)?$', UserProfileUpdate.as_view(), name="url_edit_profile"),

    # review record
    url(r'^(?P<slug>[\w\-]+)/review(/)?$', UserProfileReview.as_view(), name="url_review_profile"),
    )


# reference to plain variable (which is a CLASS) from views.py
#urlpatterns = patterns('PROFILE.views', url(r'$', 'display_data', name='url_display_data'),)
