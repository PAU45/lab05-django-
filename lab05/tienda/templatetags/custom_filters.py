from django import template

register = template.Library()

@register.filter
def length_is(value, arg):
    """Devuelve True si la longitud de 'value' es igual a 'arg'."""
    return len(value) == arg