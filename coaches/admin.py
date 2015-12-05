from django.contrib import admin
from django.contrib.auth.models import User

from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'gender', 'skype', 'description']
    list_filter = (('user__is_staff', admin.BooleanFieldListFilter),)


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'gender', 'skype', 'description']
    fields = ['username', 'password', 'first_name',
              'last_name', 'email', 'is_staff']
    list_filter = (('is_staff', admin.BooleanFieldListFilter),)

    def gender(self, obj):
        return obj.coach.gender

    def skype(self, obj):
        return obj.coach.skype

    def description(self, obj):
        return obj.coach.description


admin.site.register(Coach, CoachAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
