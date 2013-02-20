from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from PROFILE.models import UserProfile, CreateUserForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.utils.datastructures import SortedDict # for unquestionable control of entry order in template

# this one is twisted use: in order to keep in-line with single-template CRU(-D) template. 
# It returns fields:values dictionary. 
from django.forms.models import model_to_dict  

class UserProfileList(ListView):
    """List all users on paginated list"""

    # model = UserProfile
    queryset = UserProfile.objects.all().order_by('first_name')
    context_object_name = 'arpaso_profiles'
    template_name = 'userdata.html'
    paginate_by = 4


class UserProfileCreate(CreateView):
    """Ceate New UserProfile - in a form"""

    model = UserProfile
    template_name = 'profile_CRU.html'
    success_url = "/"   
        

class UserProfileUpdate(UpdateView):
    """Update specific user's information in database - in a form"""

    model = UserProfile 
    template_name = 'profile_CRU.html'
    success_url = "/" 


class UserProfileReview(DetailView):
    """Review UserProfile you just edited"""

    model = UserProfile 
    template_name = 'profile_CRU.html'
    context_object_name = 'context'

    # without context, we end up using only entries, no titles, NO DICT but flat list of fields.
    def get_context_data(self, **kwargs):
        the_profile = kwargs
        userinfo = [model_to_dict(value, exclude=['id', 'slug', 'date_added_to_db']) for value in the_profile.values()][0]

        for key, info in userinfo.items():
            # if there's no data associated (value empty), do not display empty string.
            if not userinfo[key]:
                userinfo.__delitem__(key)

        # Keys cannot be changed. Add a new key with the modified value then remove the old one, or create a new dict with a dict comprehension or the like.
        # just becuase django is NOT using sorted dict when handling models... and we want as less logic as possible in template
        # it must go ordered this way: 1.first 2.last 3.birthdate 4.country 6.contacts 5.bio 
        sorted_fields = SortedDict({
            'first_name' : userinfo['first_name'],
            'last_name' : userinfo['last_name'],
        })
        
        # lot of calculations(going over and over keys) here - for large dbs that's ineffective
        if 'date_of_birth' in userinfo.keys():
            sorted_fields.__setitem__("birth_date", userinfo['date_of_birth'])
        if 'country' in userinfo.keys():
            sorted_fields.__setitem__("country", the_profile['object'].get_country_display()) # did not work in template as this is not the object but dictionary we iterate on 
        if 'contacts' in userinfo.keys():
            sorted_fields.__setitem__("contacts", userinfo['contacts'])
        if 'biography' in userinfo.keys():
            sorted_fields.__setitem__("biography", userinfo['biography'])

        # sorted_fields.keyOrder.reverse() - here we might have an answer for upcoming task, let's inspect that later 
        return { 'context' : sorted_fields }



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