from django.contrib import admin

# Register your models here.

from .models import testout

class testoutAdmin(admin.ModelAdmin):
    list_display = ('name','age')

admin.site.register(testout, testoutAdmin)