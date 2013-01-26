=== ARPASO.COM TEST TASK ===

1. Create django project.
Create profile app (first name, last name, data of birth, biography, contacts) (((((((((( models.Model ))))))))))
Add front page, where you'll show your profile datas. (use fixtures) ((((((( initial.json )))))))


 2. Add authentication of this page
@user_passes_test(myfunc-true-false, p.313)
https://docs.djangoproject.com/en/dev/topics/auth/

 3. Create middleware, that stores all database requests.

 4. Create template context processor that adds django.conf.settings to context
https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATE_CONTEXT_PROCESSORS
https://docs.djangoproject.com/en/dev/ref/templates/api/


 5. Create a page where you may change your profile (((((( create_update ))))))

 6. forms-widgets - assign calendar widget to "date of birth" field.
 http://stackoverflow.com/questions/6485392/how-to-have-calendar-thing-in-django-date-field
 https://docs.djangoproject.com/en/1.0/topics/forms/media/

http://stackoverflow.com/questions/38601/using-django-time-date-widgets-in-custom-form
---->  self.fields['mydate'].widget = widgets.AdminDateWidget()
http://larin.in/archives/165


 7. forms-model-extra - ( "edit profile form" (paragraph_5) has been done with forms.ModelForm?) > invert field's order
 keyOrder for base_fields (Sorted_dict)  /////  fields_list.reverse() << "fields" list

 8. template-tags - create template tag, {% template_tag %} that gets any model object, and renders a link of change view in admin interface 
 ( for example: {% edit_list request.user %})
 http://djbook.ru/rel1.4/howto/custom-template-tags.html?highlight=custom%20template%20tags
 http://stackoverflow.com/questions/5586774/django-template-filters-tags-simple-tags-and-inclusion-tags
 http://stackoverflow.com/questions/1480556/django-templatetag
 p.330

 9. commands - create django command that prints all models and object counts.
 https://docs.djangoproject.com/en/dev/howto/custom-management-commands/
 http://andrewwilkinson.wordpress.com/2009/03/06/creating-django-management-commands/

 10. signals - create signal handler, that creates a note in database when every model is creating/editing/deleting.
http://www.turnkeylinux.org/blog/django-signals
http://docs.djangoproject.com/en/dev/topics/signals/

I suggest you do as follows:

  * create a repo in github
  * commit so frequently as possible.
  * type all tasks in Issues, estimate them
  * after completion of every task type real time
  * all tasks should be covered by tests.
  http://blog.openquality.ru/python-unittest/