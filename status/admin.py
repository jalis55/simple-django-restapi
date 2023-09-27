from django.contrib import admin
from status.models import Status

# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["text", "created_at", "user"]


admin.site.register(Status, StatusAdmin)
