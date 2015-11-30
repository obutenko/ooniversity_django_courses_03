from django.contrib import admin
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'skype', 'description']
    list_filter = ['gender', 'user__is_staff']

# Register your models here.
admin.site.register(Coach, CoachAdmin)
