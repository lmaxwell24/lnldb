import re

from django import template
from django.conf import settings

numeric_test = re.compile(r"^\d+$")
register = template.Library()


def getattribute(value, arg):
    """Gets an attribute of an object dynamically from a string name"""

    assert hasattr(value, str(arg)), "Invalid %s in %s" % (arg, value)
    return getattr(value, str(arg))


register.filter('getattribute', getattribute)


@register.filter
def get_item(dictionary, key):
    """Gets an item from a dictionary dynamically by key"""
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return None

