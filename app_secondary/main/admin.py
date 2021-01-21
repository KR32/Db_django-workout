from django.contrib import admin
from tinymce.widgets import TinyMCE

# Register your models here.
from .models import *

admin.site.site_header = "OHR Administration."


@admin.register(testout)
class MainAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }


class testoutAdmin(admin.ModelAdmin):
    # list_display = ('name','age', 'phone_number')
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language", "comments")


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        "currency_name",
        "country_name",
        "currency_code",
        "currency_symbol",
        "comments",
    )
    exclude = ("currency_id",)
    search_fields = (
        "country_name",
        "currency_name",
        "currency_code",
    )
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }


@admin.register(country_information)
class CountryInformationAdmin(admin.ModelAdmin):
    list_display = (
        "country_name",
        "nationality",
        "dailing_code",
        # 'currency_id',
        # 'language_id'
    )


@admin.register(section_template)
class SectionTemplateAdmin(admin.ModelAdmin):
    list_display = ("section_name",)
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }
    # exclude = ('section_id',)


@admin.register(JobDescriptionTemplate)
class JobDescTemplateAdmin(admin.ModelAdmin):
    list_display = ("description_title",)
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }
    # exclude = ('job_desc_id',)


@admin.register(PqrDetail)
class PQRDetailTemplateAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "surgical",
        "min_years_exp",
        "min_years_exp_for_nationals",
        "specialist_registration_held",
        "specialist_reg_required_for_nationals",
        "specialist_registration_years",
        "check_equivalence",
        "comments",
    )


@admin.register(PqrHeader)
class PQRHeaderAdmin(admin.ModelAdmin):
    list_display = (
        "country_id",
        "issue_authority_id",
        "pqr_name",
        "issue_date",
        "version_no",
        "description",
        "comments",
    )


@admin.register(IssueAuthority)
class IssueAuthorityAdmin(admin.ModelAdmin):
    list_display = (
        "authority_name",
        "acronym",
        "address",
        "website",
        "description",
        "licensing",
        "qualification",
    )


@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = (
        "qualification",
        "qualification_level",
        "description",
        "acronym",
        "equivalent_qualification",
        "specialist_registration_reqd",
        "by_exam",
        "course_duration_reqd",
        "display_order",
    )
