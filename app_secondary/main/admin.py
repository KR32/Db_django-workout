from django.contrib import admin
from tinymce.widgets import TinyMCE
# Register your models here.
from .models import *

admin.site.site_header = 'OHR Administration.'


class MainAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget':TinyMCE()
        },
    }

class testoutAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'phone_number', 'id')


class LanguageAdmin(admin.ModelAdmin):
    list_display =(
        'language',
        'comments'
    )

class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'currency_name',
        'country_name',
        'currency_code',
        'currency_symbol',
        'comments'
    )
    exclude = ( 
        'currency_id',
    )
    formfield_overrides = {
        models.TextField: {
            'widget':TinyMCE()
        },
    }

class CountryInformationAdmin(admin.ModelAdmin):
    list_display =(
        'country_name',
        'nationality',
        'dailing_code',
        # 'currency_id',
        # 'language_id'
    )

class SectionTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'section_name',
    )
    formfield_overrides = {
        models.TextField: {
            'widget':TinyMCE()
        },
    }
    # exclude = ('section_id',)
    
class JobDescTemplateAdmin(admin.ModelAdmin):
    list_display = (    
        'description_title',
    )
    formfield_overrides = {
        models.TextField: {
            'widget': TinyMCE()
        },
    }
    # exclude = ('job_desc_id',)


admin.site.register(testout, MainAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(country_information, CountryInformationAdmin)
admin.site.register(section_template, SectionTemplateAdmin)
admin.site.register(JobDescriptionTemplate, JobDescTemplateAdmin)