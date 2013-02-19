from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from PROFILE.models import UserProfile, CreateUserForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, UpdateView, CreateView, DetailView

# this one is twisted use: in order to keep in-line with single-template CRUD template. 
# It returns fields:values dictionary. 
from django.forms.models import model_to_dict  

# RequestContext was initially used for serving static css (hmm.)

# class-based generic view (supposed to be faster than manual methods)
#
# display_data = ListView.as_view(
#           queryset=UserProfile.objects.all(),
#           context_object_name='arpaso_profiles',
#           template_name='userdata.html',
#           )

# class-based view v2 - elegant!    ----- http://ccbv.co.uk/projects/Django/1.4/django.views.generic.list/ListView/ -----
class UserProfileList(ListView):
    """List all users on paginated list"""
    def __init__(self):
        super(UserProfileList, self).__init__()

    # model = UserProfile
    queryset = UserProfile.objects.all().order_by('first_name')
    context_object_name = 'arpaso_profiles'
    template_name = 'userdata.html'
    paginate_by = 4


class UserProfileCreate(CreateView):
    """Ceate New UserProfile in a form"""
    def __init__(self):
        super(UserProfileCreate, self).__init__()

    model = UserProfile 
    template_name = 'profile_CRU.html'
    success_url = "/"   
        

class UserProfileUpdate(UpdateView):
    """Update specific user's information in database"""
    def __init__(self):
        super(UserProfileUpdate, self).__init__()

    model = UserProfile 
    template_name = 'profile_CRU.html'
    success_url = "/" 

'''
def UserProfileReview(request, slug):
    """Absolutely equal to Update_class, above"""

    from django.shortcuts import render, get_object_or_404
    class UserProfileForm(ModelForm):
        class Meta:
            model = UserProfile

    model = get_object_or_404(UserProfile, slug=slug)
    form = UserProfileForm(instance=model)

    return render(request, 'profile_CRU.html', { 'form': form })
'''

class UserProfileReview(DetailView):
    """Review UserProfile you just edited"""
    def __init__(self):
        super(UserProfileReview, self).__init__()

    model = UserProfile 
    template_name = 'profile_CRU.html'

    def get_context_data(self, **kwargs):
        userinfo = [model_to_dict(value, exclude=['slug', 'date_added_to_db', 'id']) for value in kwargs.values()][0]
        return { 'context' : userinfo }


# old-style views
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