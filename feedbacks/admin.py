from django.contrib import admin
from feedbacks.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('from_email','time')

	def time(self, obj):
		return obj.create_date.time()

admin.site.register(Feedback, FeedbackAdmin)