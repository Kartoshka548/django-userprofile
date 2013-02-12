#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings

def Add_Settings(request):
    """Adding django.conf.settings to template context dictionary.

        The interface for a context processor is quite simple; it’s nothing more than a standard Python function 
        that takes a request as its only argument, and returns a dictionary of data to be added to the template’s context. 
        It should never raise an exception, and if no new variables need to be added, based on the specified request, 
        it should just return an empty dictionary.
    """
    #for s in dir(settings):
    #    print s, ':', getattr(settings, s)

    return {    'settings' : settings }