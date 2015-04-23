from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from checkin import Person, Device
from foro.models.user import User


class PresonAdmin(ImportExportModelAdmin):
    search_fields = ('national_id', 'fist_name', 'last_name')
    list_display = ('national_id', 'fist_name', 'last_name', 'asistencia')
    list_filter = ('asistencia',)

    pass


class DeviceAdmin(ImportExportModelAdmin):

    list_display = ('serial', 'device', 'owner')
    list_display_links = ('serial',)
    raw_id_fields = ('owner',)

    pass


class UserAdmin(admin.ModelAdmin):

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_display_links = ('username',)

    pass

admin.site.register(Person, PresonAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(User, UserAdmin)
