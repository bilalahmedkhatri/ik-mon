from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    tag = models.CharField(max_length=120)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class MonitorThumbnail(models.Model):
    tag = models.CharField(max_length=50)
    last_thumpnail = models.ImageField(upload_to='static/media/thumbnails/')
    status = models.BooleanField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.tag


class RecordedVideos(models.Model):
    tag = models.CharField(max_length=50)
    video = models.FileField(upload_to='static/media/videos/')
    status = models.BooleanField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.tag


class UserMonitor(models.Model):
    user_name = models.CharField(
        max_length=255, unique=True, null=True, blank=True)
    verification_code = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    video_url = models.CharField(max_length=100, default="")
    thumb_url = models.CharField(max_length=100, default="")
    # ip_address_ = models.IntegerField(blank=True, null=True)
    image_thumpnail = models.ForeignKey(
        MonitorThumbnail, on_delete=models.CASCADE)
    videos = models.ForeignKey(RecordedVideos, on_delete=models.CASCADE)
    os = models.CharField(max_length=100, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # extra_field = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name


class NewTest(models.Model):
    fname = models.CharField(max_length=22)

    def __str__(self) -> str:
        return self.fname
