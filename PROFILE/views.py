from django.template import loader, RequestContext
from django.http import HttpResponse
from PROFILE.models import UserProfile

def display_data(request):
    profiles = UserProfile.objects.all()
    a_template = loader.get_template("userdata.html")
    a_context = RequestContext(request, { "arpaso_profiles" : profiles })
    return HttpResponse(a_template.render(a_context))