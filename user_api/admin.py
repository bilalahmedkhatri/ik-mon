from django.contrib import admin
from .models import UserMonitor, RecordedVideos, MonitorThumbnail, Category

# Register your models here.


@admin.register(UserMonitor)
class AdminUserMonitor(admin.ModelAdmin):
    list_display = ["user_name", "verification_code", "ip_address",
                    "image_thumpnail", "videos", "os", "date_create", "date_update"]


@admin.register(RecordedVideos)
class AdminRecordedVideos(admin.ModelAdmin):
    list_display = ["tag", "video", "status", "create_at", "update_at"]


@admin.register(MonitorThumbnail)
class AdminMonitorhumbnail(admin.ModelAdmin):
    list_display = ["tag", "last_thumpnail",
                    "status", "create_at", "update_at"]


@admin.register(Category)
class AdminMonitorhumbnail(admin.ModelAdmin):
    list_display = ["name", "description",
                    "tag", "created_at", "updated_at"]
