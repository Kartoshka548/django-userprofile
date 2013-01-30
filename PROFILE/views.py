from django.template import loader, Context
from django.http import HttpResponse
from PROFILE.models import UserProfile

def display_data(request):
    profiles = UserProfile.objects.all()
    a_template = loader.get_template("userdata.html")
    a_context = Context({ "arpaso_profiles" : profiles })
    return HttpResponse(a_template.render(a_context))