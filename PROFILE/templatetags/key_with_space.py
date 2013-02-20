from django import template

register = template.Library()


#@register.simple_tag
#def dictionary_key_lookup(dictionary, key):
#   # Try to fetch a value from the dict, and if lookup failed (no such key), return an empty string.
#   return dictionary.get(key, '')

@register.filter
def strip_underscores(context):
    return context.replace("_", " ")
