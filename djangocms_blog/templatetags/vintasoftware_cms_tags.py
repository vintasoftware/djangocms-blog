from django import template

register = template.Library()


@register.filter
def replace_character(character):
    return character.replace(' ','%20').replace('?','%3F')
