from django.contrib import admin
from .models import Category, Draft, Person



class DraftAdmin(admin.ModelAdmin):

    list_display = ('product_name', 'company_name', 'status',  'is_active')


admin.site.register(Category)
admin.site.register(Draft, DraftAdmin)
admin.site.register(Person)


