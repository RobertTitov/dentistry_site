from django.contrib import admin
from .models import *


class PricesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'cat')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price', 'cat')

class CotegoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Prices, PricesAdmin)
admin.site.register(Cotegory, CotegoryAdmin) 




