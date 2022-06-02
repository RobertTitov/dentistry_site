from django import template
from main.models import Cotegory

register = template.Library()


@register.simple_tag()
def get_categories():
    return Cotegory.objects.all()


@register.inclusion_tag('main\list_categories.html')
def show_categories():
    cotegories = Cotegory.objects.all()
    return {'cotegories' : cotegories}
