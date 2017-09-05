from django import template
from bs4 import BeautifulSoup

register = template.Library()


@register.filter
def replace_character(character):
    return character.replace(' ','%20').replace('?','%3F')


@register.filter
def get_post_image(post):
    get_post = BeautifulSoup(post, 'html.parser')
    return get_post.img['src']
