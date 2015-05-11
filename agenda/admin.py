from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from django.db import models
from .models import CalendarEvent

class CalendarEventAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(CalendarEvent, CalendarEventAdmin)
