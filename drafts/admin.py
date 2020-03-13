from django.contrib import admin
from .models import Draft, Person, Category

class DraftAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'company_name', 'status', 'person', 'is_active')


admin.site.register(Category)
admin.site.register(Person)
admin.site.register(Draft, DraftAdmin)

