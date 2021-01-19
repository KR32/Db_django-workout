from django.contrib import admin
from tinymce.widgets import TinyMCE
# Register your models here.
from .models import *



class MainAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget':TinyMCE()
        },
    }
class testoutAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'phone_number', 'id')

admin.site.register(testout, MainAdmin)
admin.site.register(Language)
admin.site.register(country_information)