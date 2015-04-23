from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from checkin import Person, Device


class PresonAdmin(admin.ModelAdmin):
    search_fields = ('national_id', 'fist_name', 'last_name')
    list_display = ('national_id', 'fist_name', 'last_name', 'asistencia')
    list_filter = ('asistencia',)

    pass


class DeviceAdmin(admin.ModelAdmin):

    list_display = ('serial', 'device', 'owner')
    list_display_links = ('serial',)
    raw_id_fields = ('owner',)

    pass


admin.site.register(Person, PresonAdmin)
admin.site.register(Device, DeviceAdmin)
