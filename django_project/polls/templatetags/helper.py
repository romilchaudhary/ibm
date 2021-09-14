from django import template

register = template.Library()


@register.simple_tag
def convert_to_lower(data):
    return data.lower()


@register.simple_tag()
def first_word(text):
    return text.split()[0]

@register.simple_tag(name="upper_text_name")
def upper_text(text):
    return text.upper()


@register.filter()
def add_str(arg1, arg2):
    return arg1 + " " + arg2