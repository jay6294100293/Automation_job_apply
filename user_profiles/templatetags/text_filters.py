from django import template

register = template.Library()


@register.filter(name='split')
def split_string(value, key=';'):
    """A custom template filter to split strings by a delimiter."""
    return value.split(key)
