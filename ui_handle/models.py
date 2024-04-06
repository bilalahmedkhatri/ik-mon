from django.db import models
# Create your models here.


class ModelMonitorThumbnail(models.Model):
    tag = models.CharField(max_length=50)
    last_thumpnail = models.ImageField(upload_to='static/media/thumbnails/')
    status = models.BooleanField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.tag

   
class ModelRecordedVideos(models.Model):
    tag = models.CharField(max_length=50)
    video = models.FileField(upload_to='static/media/videos/')
    status = models.BooleanField()
    create_at=models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.tag


class ModelUserMonitor(models.Model):
    UserName = models.CharField(max_length=255, null=True, blank=True)
    verification_code = models.CharField(max_length=255)
    ip_address = models.IntegerField(blank=True, null=True)
    image_thumpnail = models.ForeignKey(ModelMonitorThumbnail, on_delete=models.CASCADE)
    Videos = models.ForeignKey(ModelRecordedVideos, on_delete=models.CASCADE)
    os = models.CharField(max_length=255, blank=True, null=True)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    extra_field = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.UserName

   
 