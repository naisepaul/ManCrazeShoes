from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    ''' Return subtotal for items '''
    return price * quantity
