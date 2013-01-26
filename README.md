=== ARPASO.COM TEST TASK ===

1. Create django project.
Create profile app (first name, last name, data of birth, biography, contacts)
Add front page, where you'll show your profile datas. (use fixtures)

2. Add authentication of this page

3. Create middleware, that stores all database requests.

4. Create template context processor that adds django.conf.settings to context

5. Create a page where you may change your profile

6. forms-widgets - assign calendar widget to "date of birth" field.

7. forms-model-extra - ( "edit profile form" (paragraph_5) has been done with forms.ModelForm?) > invert field's order

8. template-tags - create template tag, {% template_tag %} that gets any model object, and renders a link of change view in admin interface 

9. commands - create django command that prints all models and object counts.

10. signals - create signal handler, that creates a note in database when every model is creating/editing/deleting.


It's best if these criterias are met:

  * create a repo in github
  * commit so frequently as possible.
  * type all tasks in Issues, estimate them
  * after completion of every task type real time it took
  * all tasks should be covered by tests.
