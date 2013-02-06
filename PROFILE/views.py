from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from PROFILE.models import UserProfile, CreateUserForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response

def display_data(request):
    profiles = UserProfile.objects.all()
    a_template = loader.get_template("userdata.html")
    a_context = RequestContext(request, { "arpaso_profiles" : profiles })
    return HttpResponse(a_template.render(a_context))

# RequestContext was initially used for serving static css (hmm.)

def create_new_user(request):

    # Scenario A: Form filled.
    if request.method == 'POST':
        # form has been filled.
        new_user=CreateUserForm(request.POST)
        if new_user.is_valid(): # VALIDATIONS: clean_username() and clean() from models.py executed here 
            # And.... was it filled correctly?
            new_user.save()
            # let's also log new subscriber in. 
            auth_user = authenticate(username=request.POST["username"], password=request.POST["password"])
            if auth_user is not None:
                login(request, auth_user)      
                # and redirect to our sacred load of hotties.   
                return HttpResponseRedirect('/')

    # Scenario B: Form filled, but is_valid() failed...
        # Houston, we have a problem: duplicate username or passwords mismatch! Destroy evidences (Fix errors)
        return render_to_response('new_user.html', {'form': new_user }, context_instance=RequestContext(request))

    # Scenario C: new recruit coming!
    else:   
        # normal rendering of new subscriber
        inputs = CreateUserForm()
        a_template = loader.get_template("new_user.html")
        a_context = RequestContext(request, { "form" : inputs })
        return HttpResponse(a_template.render(a_context))